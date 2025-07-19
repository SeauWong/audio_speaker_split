
import argparse
from pyannote.audio import Pipeline
from pydub import AudioSegment
import os
from dotenv import load_dotenv

# 解析命令行参数
def parse_args():
    parser = argparse.ArgumentParser(description="MP3说话人分离与提取工具")
    parser.add_argument('--input', required=True, help='输入MP3文件路径')
    parser.add_argument('--output_dir', default='output', help='输出目录')
    return parser.parse_args()


def diarize_and_split(input_path, output_dir):
    load_dotenv()
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    if not hf_token:
        raise RuntimeError("请在.env文件中设置HUGGINGFACE_TOKEN")
    print("加载分离模型...")
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.0", use_auth_token=hf_token)
    diarization = pipeline(input_path)
    audio = AudioSegment.from_file(input_path)

    os.makedirs(output_dir, exist_ok=True)
    speakers = set(label for _, _, label in diarization.itertracks(yield_label=True))
    print(f"检测到说话人: {speakers}")

    # 按说话人分割音频
    for speaker in speakers:
        speaker_audio = AudioSegment.empty()
        for turn, _, label in diarization.itertracks(yield_label=True):
            if label == speaker:
                segment = audio[int(turn.start * 1000):int(turn.end * 1000)]
                speaker_audio += segment
        out_path = os.path.join(output_dir, f"{speaker}.mp3")
        speaker_audio.export(out_path, format="mp3")
        print(f"导出: {out_path}")
    print("分离完成。请试听各音轨，判断发言人。")

if __name__ == "__main__":
    args = parse_args()
    diarize_and_split(args.input, args.output_dir)
