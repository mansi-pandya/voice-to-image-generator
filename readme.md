# 🎤 Speech-to-Image Generator

A Python-based AI application that converts speech into AI-generated images. The application listens to voice input in any language, translates it into English, generates an image using Pollinations AI, and automatically opens the generated image.

## ✨ Features

- 🎙️ Speech-to-Text using microphone
- 🌍 Supports multiple languages
- 🔄 Automatic translation to English
- 🖼️ AI image generation from speech
- 💾 Saves the generated image
- 👀 Automatically opens the generated image
- 🆓 Uses Pollinations AI (No API key required)

## 🛠️ Technologies Used

- Python
- Pollinations AI
- SpeechRecognition
- Deep Translator
- Requests
- PyAudio
- urllib
- OS Module

## 📁 Project Structure

```
Speech-to-Image-Generator/
│
├── generate_img.py
├── voice_translator.py
├── generated_image.png
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. The user speaks into the microphone.
2. Speech is converted into text.
3. The detected language is automatically translated into English.
4. The translated prompt is sent to Pollinations AI.
5. An AI-generated image is created.
6. The image is saved as `generated_image.png`.
7. The generated image opens automatically.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Speech-to-Image-Generator.git
cd Speech-to-Image-Generator
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python generate_img.py
```

When prompted:

```
Describe what you want?
```

Speak naturally in any language.

### Example

**Voice Input**

```
A beautiful red rose in a glass vase
```

The application will:

- Convert speech into text
- Translate it into English (if needed)
- Generate an AI image
- Save it as `generated_image.png`
- Open the image automatically

## 🔄 Workflow

```
User Voice
      │
      ▼
Speech Recognition
      │
      ▼
Language Translation
      │
      ▼
English Prompt
      │
      ▼
Pollinations AI
      │
      ▼
Generated Image
      │
      ▼
Image Opens Automatically
```

## 📦 Requirements

- Python 3.10+
- Internet Connection
- Working Microphone

## 💡 Future Improvements

- Streamlit or React web interface
- Image history
- Download generated images
- Image style selection
- Voice command history
- Image editing support

## 📄 License

This project is created for educational and learning purposes.

## 👨‍💻 Author

Mansi

B.Tech Computer Science and Engineering Student