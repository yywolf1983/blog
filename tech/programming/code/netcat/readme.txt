将patch拷贝到cygwin中netcat的目录外，执行

patch -p0 < netcat-cygwin.patch

改用./configure --build="i686"