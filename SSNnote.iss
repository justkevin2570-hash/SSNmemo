[Setup]
AppName=SSNnote
AppVersion=0.2
AppPublisher=justkevin2570
DefaultDirName={autopf}\SSNnote
DefaultGroupName=SSNnote
OutputDir=dist
OutputBaseFilename=SSNnote_Setup
Compression=lzma
SolidCompression=yes
CloseApplications=yes
AppId={{12345678-1234-1234-1234-123456789012}}
VersionInfoVersion=0.2.0.0
VersionInfoProductName=SSNnote
VersionInfoCompany=justkevin2570
VersionInfoFileDescription=SSNnote - 스티커 메모 앱
VersionInfoProductVersion=0.2
VersionInfoOriginalFileName=SSNnote_Setup.exe

[Languages]
Name: "korean"; MessagesFile: "compiler:Languages\Korean.isl"

[Files]
Source: "dist\SSNnote\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SSNnote"; Filename: "{app}\SSNnote.exe"
Name: "{group}\{cm:UninstallProgram,SSNnote}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\SSNnote"; Filename: "{app}\SSNnote.exe"

[Run]
Filename: "{app}\SSNnote.exe"; Description: "{cm:LaunchProgram,SSNnote}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: dirifempty; Name: "{app}"
