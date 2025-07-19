# audio_speaker_split

本项目用于对包含多说话人的MP3音频进行说话人分离，并可提取指定说话人的音频片段。

## 功能
- 说话人分离（基于 pyannote.audio）
- 提取指定说话人音频

## 快速开始
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 运行主程序：
   ```bash
   python main.py --input your_audio.mp3
   ```

## 依赖
- pyannote.audio
- pydub
- torch


- onnxruntime

## Hugging Face 授权说明

本项目依赖 pyannote.audio 的预训练模型，首次运行时需要从 Hugging Face Hub 拉取模型。部分模型为受限（gated/private）资源，需提前授权，否则会报错。

**授权步骤：**
1. 注册并登录 [Hugging Face](https://hf.co/)
2. 访问 [https://hf.co/settings/tokens](https://hf.co/settings/tokens) 创建一个 Access Token（选择“Read”权限）
3. 访问下列模型页面，点击“Access repository”或“同意协议”按钮，完成授权：
   - https://hf.co/pyannote/speaker-diarization-3.0
   - https://hf.co/pyannote/segmentation-3.0
4. 将 token 写入 `.env` 文件：
   ```ini
   HUGGINGFACE_TOKEN=你的token
   ```
5. 重新运行主程序。

如未授权，程序会提示模型无法下载或权限不足。
