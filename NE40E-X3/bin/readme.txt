1. Environment variable JAVA_HOME is mandatory.

2. If you want to create a signature file, the OpenPGP private key file is required.

3. How to use:


Linux:

To create a Python software package, execute the following command:
sh makeFile.sh

To create a Python software package with a signature file, execute the following command:
sh makeFile.sh [private key]

To sign only the zipped package, execute the following command:
$JAVA_HOME/bin/java -jar pkg-tool.jar -i [Directory of zipped package] -o [Directory of generated signature file] -k [Path of private key] -t python -s
eg:
$JAVA_HOME/bin/java -jar pkg-tool.jar -i /test/pkg/ -o /test/pkg -k /test/key/subkey.asc -s


Windows:

To create a Python software package, execute the following command:
makeFile.bat

To create a Python software package with a signature file, execute the following command:
makeFile.bat [private key]

To sign only the zipped package, execute the following command:
%JAVA_HOME%\bin\java -jar pkg-tool.jar -i [Directory of zipped package] -o [Directory of generated signature file] -k [Path of private key] -t python -s
eg:
%JAVA_HOME%\bin\java -jar pkg-tool.jar -i D:\tmp\test\ -o D:\tmp\test\ -k D:\tmp\test\subkey.asc -t python -s