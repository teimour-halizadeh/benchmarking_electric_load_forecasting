export CUDA_VISIBLE_DEVICES=0
list=("seed_checking_Dlinear.py" "seed_checking_LightTS.py"\
            "seed_checking_Pyraformer.py" "seed_checking_TimeMixer.py"\
            "seed_checking_ETSformer.py")

for file in "${list[@]}"; do
   python "./extended_scripts/$file"
done


export CUDA_VISIBLE_DEVICES=1
list=("seed_checking_MICN.py"\
            "seed_checking_Reformer.py" "seed_checking_TimesNet.py"\
            "seed_checking_Autoformer.py")

for file in "${list[@]}"; do
   python "./extended_scripts/$file"
done


export CUDA_VISIBLE_DEVICES=2
list=("seed_checking_FEDformer.py" "seed_checking_Mamba.py"\
            "seed_checking_SegRNN.py" "seed_checking_iTransformer.py")

for file in "${list[@]}"; do
   python "./extended_scripts/$file"
done



export CUDA_VISIBLE_DEVICES=3
list=("seed_checking_Crossformer.py" "seed_checking_Informer.py"\
            "seed_checking_PatchTST.py" "seed_checking_TSMixer.py")

for file in "${list[@]}"; do
   python "./extended_scripts/$file"
done


