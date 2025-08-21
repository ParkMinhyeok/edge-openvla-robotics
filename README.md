# OpenVLA 설치 가이드 / Installation Guide

이 문서는 OpenVLA 공식 GitHub 저장소를 기반으로, 설치 과정에서 발생할 수 있는 PyTorch 버전 충돌 문제를 해결하는 방법을 포함한 설치 가이드입니다.

This document provides an installation guide for OpenVLA, based on the official GitHub repository. It includes a specific workaround for potential PyTorch version conflicts that can occur during setup.

---

## 1. Git 설치 (선택 사항) / Install Git (Optional)

만약 `git`이 시스템에 설치되어 있지 않다면, 먼저 설치를 진행해주세요.

If you do not have `git` installed on your system, please install it first.

```bash
# Ubuntu / Debian
sudo apt-get update
sudo apt-get install git

# macOS (Homebrew 사용 시 / using Homebrew)
brew install git
```

---

## 2. Conda 가상환경 생성 및 활성화 / Create and Activate Conda Environment

프로젝트에 필요한 라이브러리들을 관리하기 위해 새로운 Conda 가상환경을 생성하고 활성화합니다.

Create and activate a new Conda virtual environment to manage the project's dependencies.

```bash
conda create -n openvla python=3.10 -y
conda activate openvla
```

---

## 3. OpenVLA 소스 코드 복제 / Clone the OpenVLA Source Code

GitHub 저장소에서 OpenVLA 소스 코드를 복제(clone)하고 해당 디렉토리로 이동합니다.

Clone the OpenVLA source code from its GitHub repository and navigate into the project directory.

```bash
git clone https://github.com/openvla/openvla.git
cd openvla
```

---

## 4. 필수 라이브러리 설치 / Install Required Dependencies

**중요:** `requirements-min.txt`를 바로 실행하면 PyTorch와 시스템의 CUDA 버전이 맞지 않아 에러가 발생할 수 있습니다. 아래 순서에 따라 설치하는 것을 강력히 권장합니다.

**IMPORTANT:** Directly installing from `requirements-min.txt` may cause errors due to version mismatches between PyTorch and your system's CUDA driver. It is highly recommended to follow the steps below in order.

### 4.1. 최소 요구사항 설치 / Install Minimal Requirements

먼저 `requirements-min.txt` 파일에 명시된 기본 라이브러리들을 설치합니다.

First, install the base libraries specified in the `requirements-min.txt` file.

```bash
pip install -r requirements-min.txt
```

### 4.2. PyTorch 재설치 (CUDA 버전에 맞게) / Reinstall PyTorch (Matching your CUDA Version)

위 과정에서 설치된 PyTorch를 제거하고, 사용자의 GPU 환경에 맞는 버전으로 다시 설치합니다.

Uninstall the version of PyTorch that may have been installed in the previous step, and then reinstall the correct version that matches your GPU environment.

1.  **기존 PyTorch 제거 / Uninstall existing PyTorch**
    ```bash
    pip uninstall torch
    ```

2.  **내 환경에 맞는 PyTorch 설치 / Install PyTorch for your environment**
    
    [PyTorch 공식 홈페이지](https://pytorch.org/get-started/locally/)에 방문하여 자신의 CUDA 버전에 맞는 설치 명령어를 확인하세요.
    
    Visit the [Official PyTorch Website](https://pytorch.org/get-started/locally/) to find the correct installation command for your specific CUDA version.

    아래는 **CUDA 12.1** 환경을 위한 예시 명령어입니다.
    
    The command below is an example for a **CUDA 12.1** environment.
    ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    ```

### 4.3. OpenCV 설치 / Install OpenCV

마지막으로, 이미지 및 비디오 처리에 필요한 OpenCV를 설치합니다.

Finally, install OpenCV, which is required for image and video processing.

```bash
pip install opencv-python
```

---

이제 OpenVLA를 실행하기 위한 모든 준비가 완료되었습니다!

Installation is now complete! You are ready to run OpenVLA.
