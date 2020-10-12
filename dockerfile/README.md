# Discuss about the ENV instruction of Dockerfile 

The question is **"When we use the ENV instruction in the dockerfile, can we can keep it in the environment after the container is built?"**

The answer is **YES**.


Here is a simple dockerfile about the ENV instruction.

```
FROM nvcr.io/nvidia/tensorrt:20.03-py3

ENV TEST_PAR=TEST_dockerfile_env
```

Let's build it.

```
docker build -t test:test .
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM nvcr.io/nvidia/tensorrt:20.03-py3
20.03-py3: Pulling from nvidia/tensorrt
Digest: sha256:3ae126dc166475795d2481938367ffc574aae52937eda5337e588367b12c09ed
Status: Downloaded newer image for nvcr.io/nvidia/tensorrt:20.03-py3
 ---> 3132ca723421
Step 2/2 : ENV TEST_PAR=TEST_dockerfile_env
 ---> Running in 08218f56550e
Removing intermediate container 08218f56550e
 ---> ccbd89fb9fa5
Successfully built ccbd89fb9fa5
Successfully tagged test:test
```

Check it in `docker images`
```
docker images
REPOSITORY                       TAG                      IMAGE ID            CREATED             SIZE
test                             test                     ccbd89fb9fa5        19 seconds ago      4.08GB
```

Run it.
```
docker run --runtime nvidia -it --name=test_env test:test /bin/bash

=====================
== NVIDIA TensorRT ==
=====================

NVIDIA Release 20.03 (build 10567415)

NVIDIA TensorRT 7.0.0 (c) 2016-2020, NVIDIA CORPORATION.  All rights reserved.
Container image (c) 2020, NVIDIA CORPORATION.  All rights reserved.

https://developer.nvidia.com/tensorrt

To install Python sample dependencies, run /opt/tensorrt/python/python_setup.sh

To install open source parsers, plugins, and samples, run /opt/tensorrt/install_opensource.sh. See https://github.com/NVIDIA/TensorRT/tree/20.03 for more information.

root@941a3e33c77e:/workspace# ls
README.md  tensorrt
root@941a3e33c77e:/workspace# echo $TEST_PAR
TEST_dockerfile_env
```

I also did another test which is using `export` directly and exit this container, and then login again. 

```
root@941a3e33c77e:/workspace# export test1111=test1111
root@941a3e33c77e:/workspace# echo $test1111
test1111
root@941a3e33c77e:/workspace# exit
exit

$ docker start test_env
test_env
$ docker exec -ti test_env /bin/bash
root@941a3e33c77e:/workspace# ls
README.md  tensorrt
root@941a3e33c77e:/workspace# echo $test1111

root@941a3e33c77e:/workspace# exit
exit
```

# Conclusion

In the past, I was thinking the ENV instruction will only be used in the process of building the image by dockerfile.
The reason is that I misunderstand that ENV is equivalent to `export` because we all know that `export` is able to be only used once if we don't write the `export` in the `.bashrc` file.

Hence, I did this simple experiment to prove it.
