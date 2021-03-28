

assert len(sys.argv) == 13
args = {
	"workspaceFolder"			: sys.argv[1],	#	/home/your-username/your-project
	"workspaceFolderBasename"	: sys.argv[2],	#	your-project
	"file"						: sys.argv[3],	#	/home/your-username/your-project/folder/file.ext
	"fileWorkspaceFolder"		: sys.argv[4],	#	/home/your-username/your-project
	"relativeFile"				: sys.argv[5],	#	folder/file.ext
	"relativeFileDirname"		: sys.argv[6],	#	folder
	"fileBasename"				: sys.argv[7],	#	file.ext
	"fileBasenameNoExtension"	: sys.argv[8],	#	file
	"fileDirname"				: sys.argv[9],	#	/home/your-username/your-project/folder
	"fileExtname"				: sys.argv[10],	#	.ext
	"lineNumber"				: int(sys.argv[11]),
	"pathSeparator"				: sys.argv[12]	#	/ on macOS or linux, \\ on Windows
}

