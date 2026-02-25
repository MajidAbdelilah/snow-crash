#only clone if the john directory doesn't exist
if [ ! -d "john" ]; then
	git clone --depth 1 https://github.com/openwall/john.git
fi
cd john/src
./configure
make -j4
