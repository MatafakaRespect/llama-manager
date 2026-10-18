# llama-manager
A small, portable and efficient wrapper for llama.cpp written in Python. Unifies model downloading from Hugging Face, model quantization, benchmarking, and inference. 
# Core Features
- Portability - Run the same binaries on different hardware configurations.
- Efficiency - Uses ~60 MB of space, tens of times smaller when compared to popular programs with the same purpose.
- Usability - Contains a lot of features from similar wrappers.
- Easy to understand - contains arguments from select utilities so users don't have to dig through llama.cpp documentation.
# Binaries included
- llama-cli - Local inference using a command line
- llama-server - llama-cli, but accessed via a browser
- llama-quantize - Quantize local models
- llama-bench - Get a sneak peek of generation speed before using
(Everything compiled for an x86_64 Windows target)
# Notices
- Most features aren't polished yet.
- The program utilizes the CPU backend only (with basic AVX support).
- I'm a beginner at coding, so don't expect everything to be perfect at release.
- This program includes parts of [Easy-Quant](https://github.com/krystianowak/Easy-Quant). It will reach its EOL in version v0.0.5 and development will move here.
