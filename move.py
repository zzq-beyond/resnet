import os

root = "./Data/train"
opt = "tulips"

ls = os.listdir(os.path.join(root, opt))
for x in ls[:100]:
    os.system(f"mv /home/zzq/code/resnet/Data/train/{opt}/{x} /home/zzq/code/resnet/Data/val/{opt}/{x}")
    print("Done!")