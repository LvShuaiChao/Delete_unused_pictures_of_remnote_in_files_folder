只需要更改json_file和files_path的路径，即可开始删除RemNote中未使用但是Files文件夹依然保存着的图片

不过这个代码现在还不完善，有些Bug还未解决，不建议非专业用户直接开始使用。

问题有：
json文件中%LOCAL_FILE%一共出现了1267次，files文件夹中的文件一共有1543个，1543-1267=276，但是Python程序，计数属于file但不属于json的文件个数，发现是324个，324-276=48个，有48个文件，自己说不清其到底是在哪，怎么冒出来的
