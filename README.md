## safemotion/bm_safemotion/action_rnd/action/examples/deep_sort_yolov3

원본 원격저장소 : [deep_sort_yolov3](https://github.com/Qidian213/deep_sort_yolov3) (이하 DSY라고 함)

### 버전 정보 요약

![Image](https://www.evernote.com/shard/s542/sh/29287923-0edd-4705-9891-a4c756652d4e/c1c8c1ffef52844c/res/378cfbfb-2599-4941-a392-bfa39bc16df3/book-2929646.jpg)


    Anacoda         : 4.6.11
    cuda            : 9.0
    cudnn           : 7.0.5
    python          : 3.6.6

    OpenCV          : 4.0.0.21
    Tensorflow-gpu  : 1.13.1
    Keras-gpu       : 2.2.4

### 서브모듈로 추가된 deep_sort_yolov3을 로컬저장소에 클론하기

    $ cd action              # 루트디렉토리로 이동

    $ git submodule init     # 비어있는(새로 추가된) 서브모듈 초기화(등록)
    
    $ git submodule update   # 새로 등록된 서브모듈을 클론

### 케라스 설치 및 데모 파일 실행

    $ conda install keras-gpu

    $ cd examples\deep_sort_yolov3\

    $ python demo.py

### 데모 파일 실행 시 아래와 같은 오류 발생하면 다음과 같이 텐서플로우를 재설치 후 업그레이드한다.
   (※ 설치된 cuda 라이브러리와 가상환경의 cuda 패키지 버전을 동일하게 맞춰야 한다)

   ImportError: cannot import name 'abs'

    $ pip uninstall tensorflow
    $ pip uninstall tensorflow-gpu
    $ pip uninstall protobuf

    $ conda install tensorflow-gpu=1.12
    Collecting package metadata: done
    Solving environment: done

    ## Package Plan ##

    environment location: C:\Anaconda3\envs\action

    added / updated specs:
        - tensorflow=1.12

    The following packages will be downloaded:

        package                    |            build
        ---------------------------|-----------------
        tensorboard-1.12.2         |   py36h33f27b4_0         3.1 MB
        tensorflow-1.12.0          |gpu_py36ha5f9131_0           4 KB
        tensorflow-base-1.12.0     |gpu_py36h6e53903_0       180.8 MB
        tensorflow-gpu-1.12.0      |       h0d30ee6_0           3 KB
        ------------------------------------------------------------
                                            Total:       184.0 MB

    The following packages will be DOWNGRADED:

    cudatoolkit                                    10.0.130-0 --> 9.0-1
    cudnn                                    7.3.1-cuda10.0_0 --> 7.3.1-cuda9.0_0
    tensorboard                         1.13.1-py36h33f27b4_0 --> 1.12.2-py36h33f@@27b4_0
    tensorflow                      1.13.1-gpu_py36h9006a92_0 --> 1.12.0-gpu_py36ha5f9131_0
    tensorflow-base                 1.13.1-gpu_py36h871c8ca_0 --> 1.12.0-gpu_py36h6e53903_0
    tensorflow-gpu                          1.13.1-h0d30ee6_0 --> 1.12.0-h0d30ee6_0
    $ conda install tensorflow-gpu (업그레이드 - 최신버전 1.13)

### ※ cudatoolkit과 cudnn의 버전을 확인

### YOLO model을 다운로드(1, 2 과정을 수행한 keras model 파일을 다운 가능)

1. [YOLO 사이트](https://pjreddie.com/darknet/yolo/)에 접속하여 Yolov3 weights 를 다운
2. Darknet YOLO model을 keras model로 변환 : [Yolov3의 변환된 keras model 다운로드](https://drive.google.com/file/d/1uvXFacPnrSMw6ldWTyLLjGLETlEsUvcE/view)
    python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
3. 변환된 keras model을 "model_data" 폴더로 이동

### submodule 형태로 클론했으므로 model의 경로 변경

    (demo.py)
    033     #model_filename = 'model_data/mars-small128.pb'
    034     model_filename = join(dirname(abspath(dirname(abspath(dirname(__file__))))), 'lib\\deep_sort_yolov3\\model_data\\mars-small128.pb')

    (yolo.py)
    028     self.model_path = join(dirname(abspath(dirname(abspath(dirname(__file__))))), 'lib\\deep_sort_yolov3\\model_data\\yolo.h5')
    029     self.anchors_path = join(dirname(abspath(dirname(abspath(dirname(__file__))))), 'lib\\deep_sort_yolov3\\model_data\\yolo_anchors.txt')
    030     self.classes_path = join(dirname(abspath(dirname(abspath(dirname(__file__))))), 'lib\\deep_sort_yolov3\\model_data\\coco_classes.txt')
    031     #self.model_path = 'model_data/yolo.h5'
    032     #self.anchors_path = 'model_data/yolo_anchors.txt'
    033     #self.classes_path = 'model_data/coco_classes.txt'

### 데모 파일 실행한 결과 (Asus 노트북 X560U에서 6프레임 정도)

    d:\OneDrive - SM\Work\Git\action\examples\deep_sort_yolov3 (master -> origin)
    (action) λ python demo.py
    Using TensorFlow backend.
    2019-05-28 14:25:14.710854: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
    2019-05-28 14:25:15.877978: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1433] Found device 0 with properties:
    name: GeForce GTX 1050 major: 6 minor: 1 memoryClockRate(GHz): 1.493
    pciBusID: 0000:01:00.0
    totalMemory: 4.00GiB freeMemory: 3.31GiB
    2019-05-28 14:25:15.907361: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1512] Adding visible gpu devices: 0
    2019-05-28 14:25:16.494615: I tensorflow/core/common_runtime/gpu/gpu_device.cc:984] Device interconnect StreamExecutor with strength 1 edge matrix:
    2019-05-28 14:25:16.519443: I tensorflow/core/common_runtime/gpu/gpu_device.cc:990]      0
    2019-05-28 14:25:16.530119: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1003] 0:   N
    2019-05-28 14:25:16.540770: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 3018 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1050, pci bus id: 0000:01:00.0, compute capability: 6.1)
    WARNING:tensorflow:From C:\Anaconda3\envs\action\lib\site-packages\tensorflow\python\framework\op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
    Instructions for updating:
    Colocations handled automatically by placer.
    model_data/yolo.h5 model, anchors, and classes loaded.
    2019-05-28 14:25:30.767331: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1512] Adding visible gpu devices: 0
    2019-05-28 14:25:30.780374: I tensorflow/core/common_runtime/gpu/gpu_device.cc:984] Device interconnect StreamExecutor with strength 1 edge matrix:
    2019-05-28 14:25:30.795706: I tensorflow/core/common_runtime/gpu/gpu_device.cc:990]      0
    2019-05-28 14:25:30.805201: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1003] 0:   N
    2019-05-28 14:25:30.814452: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 3018 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1050, pci bus id: 0000:01:00.0, compute capability: 6.1)
    2019-05-28 14:25:35.513205: I tensorflow/stream_executor/dso_loader.cc:152] successfully opened CUDA library cublas64_90.dll locally
    fps= 0.080444
    fps= 2.132731
    fps= 4.026688
    fps= 4.901176
    fps= 5.567653
    fps= 5.834336
    fps= 6.030087
    fps= 6.169642
    fps= 6.150627


