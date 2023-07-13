This file provides and overview and instructions for running the PythonDemo2_PullVideofromWebsite project.

**Description**  
The purpose of this python script is to enable a user to select a video of their choice from YouTube,  
and download it onto a directory of choice (often on their local PC)

**Prerequisites**  

Python 3.11 Refer to the project **Requirements.txt** for the current list of libraries  
that need to be installed in order to execute this script successfully  
(in addition to those already available in Python 3.11)

Minimum Pip version: pip-23.1.2-py3

-the initial intent of this script is to have it executed on a Windows environment (.64bit)

**Installation**  
To successfully run this script, you'll need to do the following:

1.  Ensure you have Python 3.11 installed on your system  
2.  Clone the repository for yourself 'git clone https://github/  
3.  Install the required dependencies 'pip install -r Requirements.txt  
4. Make sure you have a directory defined for the downloadable file,  
  as you will be prompted for this in order to proceed with the script steps to completion.  
5. Have a desired link to a YouTube video that you will want to download a copy of  
(this is acquired via the link provided in YouTube when "Share" button is selected.)  

*-note: **Due to Git's limited ability to handle media files, be sure to exclude your downloaded video file directory in .gitignore PRIOR to testing this script,  
Otherwise, your Git history may bloat quickly!!! ** 
It is suggested that you test this script first with a short, simple video (small file size) to ensure everything is functioning properly
#Usage Upon running the script, input files and output files and paths are prompted by the script for user input. Detailed (verbose) execution commentary will be provided, as well as robust error reporting. Note: there will be comments during the execution of "files being deleted" with the option of the -k flag to keep them. These are
referring to the baseline video files (which will initially be in various formats) will be merged as part of the overall execution process,
and thus, will no longer be needed once the final, downloaded video file is created.*  

**Considerations**

Keep in mind that you will need to make sure that ffmpeg codec will be required in order to play back  
any downloaded video files.  

Please note that if **FFmpeg** is not installed on your PC, you will need to download and install it  
before you can use it to process video files.  

*The official FFmpeg website (ffmpeg.org) provides downloads and detailed installation instructions for various operating systems.*  
  
Additionally, please remember to respect the terms of service and copyright restrictions when downloading and using videos from YouTube.
Make sure you have the necessary permissions or use videos that are available under appropriate licenses.

**Video Playback Version Details**  

ffmpeg version 6.0-full_build-www.gyan.dev   
Copyright (c) 2000-2023 the FFmpeg developers built with gcc 12.2.0 (Rev10, Built by MSYS2 project) configuration:  
--enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-fontconfig   
--enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-libsnappy  
--enable-zlib --enable-librist --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-libbluray  
--enable-libcaca --enable-sdl2 --enable-libaribb24 --enable-libdav1d --enable-libdavs2 --enable-libuavs3d  
--enable-libzvbi --enable-librav1e --enable-libsvtav1 --enable-libwebp --enable-libx264 --enable-libx265  
--enable-libxavs2 --enable-libxvid --enable-libaom --enable-libjxl --enable-libopenjpeg --enable-libvpx  
--enable-mediafoundation --enable-libass --enable-frei0r --enable-libfreetype --enable-libfribidi  
--enable-liblensfun --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm  
--enable-cuvid --enable-ffnvcodec --enable-nvdec --enable-nvenc --enable-d3d11va --enable-dxva2 --enable-libvpl  
--enable-libshaderc --enable-vulkan --enable-libplacebo --enable-opencl --enable-libcdio --enable-libgme  
--enable-libmodplug --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libshine  
--enable-libtheora --enable-libtwolame --enable-libvo-amrwbenc --enable-libilbc --enable-libgsm  
--enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-ladspa --enable-libbs2b  
--enable-libflite --enable-libmysofa --enable-librubberband --enable-libsoxr --enable-chromaprint  
libavutil 58. 2.100 / 58. 2.100 libavcodec 60. 3.100 / 60. 3.100 libavformat 60. 3.100 / 60. 3.100 libavdevice 60. 1.100  
/ 60. 1.100 libavfilter 9. 3.100 / 9. 3.100 libswscale 7. 1.100 /7. 1.100  
libswresample 4. 10.100 / 4. 10.100 libpostproc 57. 1.100 / 57. 1.100
