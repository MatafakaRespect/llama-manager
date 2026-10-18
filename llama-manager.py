import os
import time
import huggingface_hub

# Welcome screen and options

print("▄▄ ▄▄")
print("██ ██")
print("██ ██  ▀▀█▄ ███▄███▄  ▀▀█▄  ▄▄▄▄  ███▄███▄  ▀▀█▄ ████▄  ▀▀█▄ ▄███▄ ▄█▀█▄ █▄██▄      ")
print("██ ██ ▄█▀██ ██ ██ ██ ▄█▀██        ██ ██ ██ ▄█▀██ ██ ██ ▄█▀██ ██  █ ██▄█▀ ██       ")
print("██ ██ ▀█▄██ ██ ██ ██ ▀█▄██        ██ ██ ██ ▀█▄██ ██ ██ ▀█▄██ ▀███▀ ▀█▄▄▄ ██     ")
print("                                                                ██              ")
print("                                                              ███▀             ")
print("")
print("    A friendly wrapper for language model inference using bare llama.cpp")
print("")

# Spent a lot of time just for the logo...

time.sleep(0.5)

while True:
    print("Available Utilities: ")
    print("")
    print("1. llama-cli - Chat with models using a command interface")
    print("2. llama-server - Graphical version of llama-cli accessed via a browser")
    print("3. llama-quantize - Quantize models to your liking")
    print("4. llama-bench - See how fast is prompt processing and token generation on your hardware")
    print("5. Hugging Face downloader - Download AI models")
    print("Q - Exit the program")
    print("")

    choice = (int and str)(input("Type in the name or number of a utility to use (or type Q to quit): "))
    print("")
   
    if choice in ("1", "llama-cli"):

        # Define path and options
    
        modelCli = str(input("Enter the absolute path for your GGUF model: "))

        print("")
        print("List of additional arguments:")
        print("-t or --threads - number of CPU threads to use for inference (default is all)")
        print("-Cr or --cpu-range - Set certain cores to use for inference (set by typing lowest and highest thread number to assign)")
        print("-b or --batch-size - maximum logical batch size to process (default is 2048)")
        print("-ub or --ubatch-size - physical maximum batch size to process (default is 512)")
        print("-c or --ctx-size - size of prompt context (default depends on the model)")
        print("-fa or --flash-attn - use Flash Attention")
        print("-p or --prompt - the prompt to start the conversation with")
        print("-ctk or --cache-type-k - K cache quantization (default is f16)")
        print("-ctv or --cache-type-v - V cache quantization (default is f16, setting same type as K is recommended)")
        print("-lm or --load-mode - loading mode of the model (toggle memory mapping (mmap) with 'mmap', disable it with 'none')")
        print("-lzm or --lazy-mode - load certain parts of the model only when needed (low memory systems may benefit from this)")
        print("-dev or --device - set device to use for inference (using definitions like dev1, dev2, and so on)")
        print("-v or --verbose or --log-verbose - enable verbose mode, useful for debugging")
        print("--temp or --temperature - controls whether the model picks more unique tokens (higher value = more creative, default is 0.8)")
        print("--top-k - top-k sampling (default is 40)")
        print("--top-p - top-p sampling (default is 0.95)")
        print("--min-p - min-p sampling (default is 0.05)")
        print("--repeat-penalty - penalize model for repeating a sequence of tokens (default is 1.0)")
        print("--presence-penalty - presence penalty (default is 0)")
        print("--frequency-penalty - frequency penalty (default is 0)")
        print("-mm or --mmproj - path for multimodal projector file")
        print("--jinja or --no-jinja - decide whether to use Jinja engine for chat")
        print("-rea or --reasoning - use the model's reasoning capabilities")
        print("")

        argsCli = str(input("Enter additional arguments for model execution: "))

        # Bundle it all together into a single variable (add "-ngl 0" to prevent crashes)

        everyArgCli = str("--model"), str(modelCli), str(argsCli), str("-ngl 0")

        # Define directories and files needed

        cliDir = os.path.dirname(os.path.abspath(__file__))
        cliPath = os.path.join(cliDir, "llama-suite", "llama-cli.exe")

        # Start the process

        os.startfile(cliPath, arguments=" ".join(everyArgCli))

        print("")

    elif choice in ("2", "llama-server"):

        # Options
        print("")
        print("List of additional arguments:")
        print("-t or --threads - number of CPU threads to use for inference (default is all)")
        print("-Cr or --cpu-range - Set certain cores to use for inference (set by typing lowest and highest thread number to assign)")
        print("-b or --batch-size - maximum logical batch size to process (default is 2048)")
        print("-ub or --ubatch-size - physical maximum batch size to process (default is 512)")
        print("-c or --ctx-size - size of prompt context (default depends on the model)")
        print("-fa or --flash-attn - use Flash Attention")
        print("-p or --prompt - the prompt to start the conversation with")
        print("-ctk or --cache-type-k - K cache quantization (default is f16)")
        print("-ctv or --cache-type-v - V cache quantization (default is f16, setting same type as K is recommended)")
        print("-lm or --load-mode - loading mode of the model (toggle memory mapping (mmap) with 'mmap', disable it with 'none')")
        print("-lzm or --lazy-mode - load certain parts of the model only when needed (low memory systems may benefit from this)")
        print("-dev or --device - set device to use for inference (using definitions like dev1, dev2, and so on)")
        print("-v or --verbose or --log-verbose - enable verbose mode, useful for debugging")
        print("--temp or --temperature - controls whether the model picks more unique tokens (higher value = more creative, default is 0.8)")
        print("--top-k - top-k sampling (default is 40)")
        print("--top-p - top-p sampling (default is 0.95)")
        print("--min-p - min-p sampling (default is 0.05)")
        print("--repeat-penalty - penalize model for repeating a sequence of tokens (default is 1.0)")
        print("--presence-penalty - presence penalty (default is 0)")
        print("--frequency-penalty - frequency penalty (default is 0)")
        print("-mm or --mmproj - path for multimodal projector file")
        print("--jinja or --no-jinja - decide whether to use Jinja engine for chat")
        print("-rea or --reasoning - use the model's reasoning capabilities")
        print("")

        argsServe = str(input("Define arguments for launching: "))

        print("")

        # Execution

        serveDir = os.path.dirname(os.path.abspath(__file__))
        servePath = os.path.join(serveDir, "llama-suite", "llama-server.exe")
        os.startfile(servePath, arguments=" ".join(argsServe))

        # IP address notice

        print("Go to the IP adress specified by the program (specified in line 'listening on [IP ADDRESS:PORT]').")
        print("")

    elif choice in ("3", "llama-quantize"):

        # A few questions and propositions

        quantPath = str(input("Enter the absolute path for the GGUF file you want to quantize: "))

        print("")
        print("All quantization types and their BPW (bits per weight, smaller number -> less compute required but worse accuracy): ")
        print("F32, 32 BPW")
        print("F16/BF16, 16 BPW")
        print("Q8_0, ~8 BPW")
        print("Q6_K, ~6.5 BPW")
        print("Q5_1, ~6 BPW")
        print("Q5_K_M, ~5.6 BPW")
        print("Q5_0, 5.5 BPW")
        print("Q5_K_S, ~5.5 BPW")
        print("Q4_1, 5 BPW")
        print("Q4_K_M, 4.8 BPW")
        print("Q4_0, 4.5 BPW")
        print("Q4_K_S, 4.3 BPW")
        print("Q3_K_L, 4.1 BPW ")
        print("Q3_K_M, ~3.9 BPW")
        print("Q3_K_S, ~3.5 BPW")
        print("Q2_K_S, ~2.75 BPW")
        print("Q2_K, ~2.6 BPW")
        print("Q2_0, ~2.25 BPW")
        print("Q1_0, ~1.12 BPW")
        print("")
        print("Importance Matrix quantization")
        print("IQ4_NL, ~4.5 BPW")
        print("IQ4_XS, ~4.25 BPW")
        print("IQ3_M, ~3.66 BPW")
        print("IQ3_S, ~3.44 BPW")
        print("IQ3_XS, ~3.3 BPW")
        print("IQ3_XXS, ~3.06 BPW")
        print("IQ2_M, ~2.7 BPW")
        print("IQ2_S, ~2.5 BPW")
        print("IQ2_XS, ~2.31 BPW")
        print("IQ2_XXS, 2.06 BPW")
        print("IQ1_M, ~1.75 BPW")
        print("IQ1_M, ~1.56 BPW")
        print("")
        print("Ternization")
        print("TQ2_0, ~2.06 BPW")
        print("TQ1_0, ~1.69 BPW")
        print("")

         
        quantType = str(input("Enter the quantization type you want to implement: "))

        print("")

        imatrixNotice = str(input("Do you want to produce an importance matrix quant (name starts with 'IQ')? [Y/N]: "))

        if imatrixNotice in ("Y", "y", "Yes", "yes"):

            print("")

            imatrixPath = str(input("Enter the absolute path for the importance matrix file: "))
             
            # Create output directory
              
            print("The file will be ready in the 'output' folder in the current directory.")

            os.makedirs("./output", exist_ok=True)
             
            print("")

            # Setting the script up for success

            quantArgs = str("--allow-requantize"), str("--imatrix"), str(imatrixPath), str(quantPath), str(f"./output/model-{quantType}.gguf"), str(quantType),

            print("Quantizing model (this may take a while)...")

            print("")
           
            quantDir = os.path.dirname(os.path.abspath(__file__))
            quantPath = os.path.join(quantDir, "llama-suite", "llama-quantize.exe")
            os.startfile(quantPath, arguments=" ".join(quantArgs))
        else:

            # Mostly the same procedure as in the last one

            print("The file will be ready in the 'output' folder in the current directory.")

            os.makedirs("./output", exist_ok=True)
             
            print("")

            quantArgs = str("--allow-requantize"), str(quantPath), str(f"./output/model-{quantType}.gguf"), str(quantType),

            print("Quantizing model (this may take a while)...")

            print("")
           
            quantDir = os.path.dirname(os.path.abspath(__file__))
            quantPath = os.path.join(quantDir, "llama-suite", "llama-quantize.exe")
            os.startfile(quantPath, arguments=" ".join(quantArgs))

    elif choice in ("4", "llama-bench"):

        # A few questions again...

        benchModel = str(input("Enter the absolute path for your model: "))

        print("")
        print("List of more important additional arguments:")
        print("--list-devices, lists devices that the benchmark is being run on")
        print("-v or --verbose, an in-depth analysis what the program is doing behind the scenes")
        print("-p or --n-prompt, how many tokens to analyze during prompt processing (default is 512)")
        print("-n or --n-gen, how many tokens to generate while benchmarking (default is 128)")
        print("-ngl or --n-gpu-layers, how many layers to process on the GPU (default is -1, so all layers on GPU)")
        print("-t, how many CPU threads to involve during the test (varies by machine)")
        print("-fa, enables Flash Attention, more efficient self-attention in models (automatic by default)")
        print("")
        benchArgs = str(input("Enter additional arguments:"))

        benchAllArgs = str("--model"), str(benchModel), str(benchArgs)
    
        print("")
        print("Benchmark started! (Pp or prompt processing = how fast can the model process your input, token generation = how fast it can output the answer.)")

        benchDir = os.path.dirname(os.path.abspath(__file__))
        benchPath = os.path.join(quantDir, "llama-suite", "llama-bench.exe")
        os.startfile(benchPath, arguments=" ".join(benchAllArgs))

    elif choice in ("5", "Hugging Face"):

        modelDownload = str(input("Enter the HF path you want to download the model from (preferably GGUF, path looks like [User]/[Model Name] on the top: "))

        print("")

        modelFilename = str(input("Some repositories contain multiple files. Enter the exact name of the file you want to download (available in the 'Files' tab on the model page): "))

        print("")
        print("Downloading model...")

        huggingface_hub.hf_hub_download(repo_id=(modelDownload), filename=(modelFilename))

        print("")

        print("Download complete! It's in 'your user folder/.cache/huggingface/hub/'.")

    elif choice in ("Q", "q"):
        break