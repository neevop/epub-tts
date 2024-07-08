# Epub-TTS
## 项目预览
从开源项目 [ChatTTS-Enhanced](https://github.com/CCmahua/ChatTTS-Enhanced) 二次开发。 持续完善中...

## 介绍

- 支持上传epub文件，按章节转换为有声书文件。
- 音质增强/降噪解决Chat-TTS生成时的噪音问题。 
- 支持多TXT、SRT文件批量处理。 
- 支持长文本处理，支持中英混读。可自定义切割长度。 
- 支持导出srt文件。
- 支持调节语速、停顿、笑声、口语化程度等参数。
- 支持导入ChatTTS Speaker音色。详情看帮助。
- 支持储存音色配置与选项配置。方便管理。

## 离线一键整合包

暂无。

## 部署

### Mac&Linux部署
```
conda create -n Dlab python=3.10
conda activate Dlab
```

Linux
```
conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=11.8 -c pytorch -c nvidia
```
Mac
```
conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 cpuonly -c pytorch
```

```
pip install resemble-enhance
pip install -r requirements.txt
pip install WeTextProcessing
```
```
python webui/webui.py
```

### 部署问题：
    - mac M1/M2暂时无法安装依赖项`WeTextProcessing`，暂未解决。


## 感谢

- ChatTTS-Enhanced:https://github.com/CCmahua/ChatTTS-Enhanced
- ChatTTS:https://github.com/2noise/ChatTTS
- Resemble Enhance:https://github.com/resemble-ai/resemble-enhance
- ChatTTS_colab:https://github.com/6drf21e/ChatTTS_colab
- PaddleSpeech:https://github.com/PaddlePaddle/PaddleSpeech
- ChatTTS_Speaker:https://github.com/6drf21e/ChatTTS_Speaker
- WeTextProcessing:https://github.com/wenet-e2e/WeTextProcessing
- frpc:https://github.com/stilleshan/frpc



