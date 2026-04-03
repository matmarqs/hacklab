# Century -- underthewire.tech

## Century 1

The password for Century2 is the build version of the instance of PowerShell installed on this system.

```powershell
PS C:\users\century1\desktop> echo $PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.14393.8422
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.14393.8422
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```

Password: 10.0.14393.8422

## Century 2

The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

```powershell
PS C:\users\century2\desktop> get-childitem


    Directory: C:\users\century2\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM            693 443
```

Password: invoke-webrequest443

## Century 3

```
PS C:\users\century3\desktop> get-childitem | measure-object


Count    : 123
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

Password: 123

## Century 4

```powershell
PS C:\users\century4\desktop> dir


    Directory: C:\users\century4\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        4/27/2025   7:57 PM                Can You Open Me


PS C:\users\century4\desktop> dir '.\Can You Open Me'


    Directory: C:\users\century4\desktop\Can You Open Me


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/27/2025   7:57 PM             24 15768
```

Password: 15768

## Century 5

```powershell
PS C:\users\century5\desktop> dir


    Directory: C:\users\century5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             54 3347


PS C:\users\century5\desktop> get-command *domain*

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Get-StorageFaultDomain                             2.0.0.0    Storage
Cmdlet          Add-ADDomainControllerPasswordReplicationPolicy    1.0.0.0    ActiveDirectory
Cmdlet          Add-ADDSReadOnlyDomainControllerAccount            1.0.0.0    ADDSDeployment
Cmdlet          Get-ADDefaultDomainPasswordPolicy                  1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomain                                       1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomainController                             1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomainControllerPasswordReplicationPolicy    1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomainControllerPasswordReplicationPolicy... 1.0.0.0    ActiveDirectory
Cmdlet          Get-WebAppDomain                                   1.0.0.0    WebAdministration
Cmdlet          Install-ADDSDomain                                 1.0.0.0    ADDSDeployment
Cmdlet          Install-ADDSDomainController                       1.0.0.0    ADDSDeployment
Cmdlet          Remove-ADDomainControllerPasswordReplicationPolicy 1.0.0.0    ActiveDirectory
Cmdlet          Set-ADDefaultDomainPasswordPolicy                  1.0.0.0    ActiveDirectory
Cmdlet          Set-ADDomain                                       1.0.0.0    ActiveDirectory
Cmdlet          Set-ADDomainMode                                   1.0.0.0    ActiveDirectory
Cmdlet          Test-ADDSDomainControllerInstallation              1.0.0.0    ADDSDeployment
Cmdlet          Test-ADDSDomainControllerUninstallation            1.0.0.0    ADDSDeployment
Cmdlet          Test-ADDSDomainInstallation                        1.0.0.0    ADDSDeployment
Cmdlet          Test-ADDSReadOnlyDomainControllerAccountCreation   1.0.0.0    ADDSDeployment
Cmdlet          Uninstall-ADDSDomainController                     1.0.0.0    ADDSDeployment
Application     domain.msc                                         0.0.0.0    C:\Windows\system32\domain.msc


PS C:\users\century5\desktop> Get-ADDomain


AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=underthewire,DC=tech
DeletedObjectsContainer            : CN=Deleted Objects,DC=underthewire,DC=tech
DistinguishedName                  : DC=underthewire,DC=tech
DNSRoot                            : underthewire.tech
DomainControllersContainer         : OU=Domain Controllers,DC=underthewire,DC=tech
DomainMode                         : Windows2016Domain
DomainSID                          : S-1-5-21-758131494-606461608-3556270690
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=underthewire,DC=tech
Forest                             : underthewire.tech
InfrastructureMaster               : utw.underthewire.tech
LastLogonReplicationInterval       :
LinkedGroupPolicyObjects           : {cn={ECB4A7C0-B4E1-41B1-9E89-161CFA679999},cn=policies,cn=system,DC=underthewire,DC=tech, CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=underthewire,DC=tech}
LostAndFoundContainer              : CN=LostAndFound,DC=underthewire,DC=tech
ManagedBy                          :
Name                               : underthewire
NetBIOSName                        : underthewire
ObjectClass                        : domainDNS
ObjectGUID                         : bdccf3ad-b495-4d86-a94c-60f0d832e6f0
ParentDomain                       :
PDCEmulator                        : utw.underthewire.tech
PublicKeyRequiredPasswordRolling   : True
QuotasContainer                    : CN=NTDS Quotas,DC=underthewire,DC=tech
ReadOnlyReplicaDirectoryServers    : {}
ReplicaDirectoryServers            : {utw.underthewire.tech}
RIDMaster                          : utw.underthewire.tech
SubordinateReferences              : {DC=ForestDnsZones,DC=underthewire,DC=tech, DC=DomainDnsZones,DC=underthewire,DC=tech, CN=Configuration,DC=underthewire,DC=tech}
SystemsContainer                   : CN=System,DC=underthewire,DC=tech
UsersContainer                     : CN=Users,DC=underthewire,DC=tech


PS C:\users\century6\desktop> echo $env:USERDOMAIN
underthewire
```

Password: underthewire3347

## Century 6

```powershell
PS C:\users\century6\desktop> get-childitem -attributes Directory | measure-object


Count    : 197
Average  :
Sum      :
Maximum  :
Minimum  :
Property :



PS C:\users\century6\desktop> get-childitem | measure-object


Count    : 197
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

## Century 7

```powershell
PS C:\users\century7\desktop> dir
PS C:\users\century7\desktop> cd ..
PS C:\users\century7> dir


    Directory: C:\users\century7


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        7/16/2016   1:23 PM                Desktop
d-r---        8/30/2018   3:10 AM                Documents
d-----        1/22/2025  10:36 PM                Downloads
d-r---        7/16/2016   1:23 PM                Favorites
d-r---        7/16/2016   1:23 PM                Links
d-r---        7/16/2016   1:23 PM                Music
d-r---        7/16/2016   1:23 PM                Pictures
d-----        7/16/2016   1:23 PM                Saved Games
d-r---        7/16/2016   1:23 PM                Videos


PS C:\users\century7> dir .\Documents
PS C:\users\century7> dir .\Downloads


    Directory: C:\users\century7\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM              7 Readme.txt


PS C:\users\century7> cat .\Downloads\Readme.txt
7points
```

## Century 8

```powershell
PS C:\users\century8\desktop> Get-Content .\unique.txt | sort-object | get-unique | measure-object


Count    : 696
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

## Century 9

```powershell
PS C:\users\century9\desktop> (get-content -delimiter " " .\Word_File.txt)[160]
pierid
```

## Century 10

```powershell
PS C:\users\century10\desktop> (get-service -name wuauserv).Description
PS C:\users\century10\desktop> sc.exe qdescription wuauserv
[SC] QueryServiceConfig2 SUCCESS

SERVICE_NAME: wuauserv
DESCRIPTION:  Enables the detection, download, and installation of updates for Windows and other programs. If this service is disabled, users of this computer will not be able to use Windows Update or its automatic updating feature, an
d programs will not be able to use the Windows Update Agent (WUA) API.

PS C:\users\century10\desktop> dir


    Directory: C:\users\century10\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM             43 110
```

Password: windowsupdates110

## Century 11

```powershell
PS C:\users\century11> get-childitem -hidden -recurse .

    Directory: C:\users\century11\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
--rh--        8/30/2018   3:34 AM             30 secret_sauce
```

## Century 12

```powershell
PS C:\users\century12\desktop> dir


    Directory: C:\users\century12\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM             30 _things


PS C:\users\century12\desktop> get-command *domain*

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Get-StorageFaultDomain                             2.0.0.0    Storage
Cmdlet          Add-ADDomainControllerPasswordReplicationPolicy    1.0.0.0    ActiveDirectory
Cmdlet          Add-ADDSReadOnlyDomainControllerAccount            1.0.0.0    ADDSDeployment
Cmdlet          Get-ADDefaultDomainPasswordPolicy                  1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomain                                       1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomainController                             1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomainControllerPasswordReplicationPolicy    1.0.0.0    ActiveDirectory
Cmdlet          Get-ADDomainControllerPasswordReplicationPolicy... 1.0.0.0    ActiveDirectory
Cmdlet          Get-WebAppDomain                                   1.0.0.0    WebAdministration
Cmdlet          Install-ADDSDomain                                 1.0.0.0    ADDSDeployment
Cmdlet          Install-ADDSDomainController                       1.0.0.0    ADDSDeployment
Cmdlet          Remove-ADDomainControllerPasswordReplicationPolicy 1.0.0.0    ActiveDirectory
Cmdlet          Set-ADDefaultDomainPasswordPolicy                  1.0.0.0    ActiveDirectory
Cmdlet          Set-ADDomain                                       1.0.0.0    ActiveDirectory
Cmdlet          Set-ADDomainMode                                   1.0.0.0    ActiveDirectory
Cmdlet          Test-ADDSDomainControllerInstallation              1.0.0.0    ADDSDeployment
Cmdlet          Test-ADDSDomainControllerUninstallation            1.0.0.0    ADDSDeployment
Cmdlet          Test-ADDSDomainInstallation                        1.0.0.0    ADDSDeployment
Cmdlet          Test-ADDSReadOnlyDomainControllerAccountCreation   1.0.0.0    ADDSDeployment
Cmdlet          Uninstall-ADDSDomainController                     1.0.0.0    ADDSDeployment
Application     domain.msc                                         0.0.0.0    C:\Windows\system32\domain.msc


PS C:\users\century12\desktop> get-addomaincontroller


ComputerObjectDN           : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DefaultPartition           : DC=underthewire,DC=tech
Domain                     : underthewire.tech
Enabled                    : True
Forest                     : underthewire.tech
HostName                   : utw.underthewire.tech
InvocationId               : 09ee1897-2210-4ac9-989d-e19b4241e9c6
IPv4Address                : 192.99.167.156
IPv6Address                :
IsGlobalCatalog            : True
IsReadOnly                 : False
LdapPort                   : 389
Name                       : UTW
NTDSSettingsObjectDN       : CN=NTDS Settings,CN=UTW,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=underthewire,DC=tech
OperatingSystem            : Windows Server 2016 Standard
OperatingSystemHotfix      :
OperatingSystemServicePack :
OperatingSystemVersion     : 10.0 (14393)
OperationMasterRoles       : {SchemaMaster, DomainNamingMaster, PDCEmulator, RIDMaster...}
Partitions                 : {DC=ForestDnsZones,DC=underthewire,DC=tech, DC=DomainDnsZones,DC=underthewire,DC=tech, CN=Schema,CN=Configuration,DC=underthewire,DC=tech, CN=Configuration,DC=underthewire,DC=tech...}
ServerObjectDN             : CN=UTW,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=underthewire,DC=tech
ServerObjectGuid           : df17c8a3-dd76-438b-8ddf-b7ad3e624618
Site                       : Default-First-Site-Name
SslPort                    : 636


PS C:\users\century12\desktop> get-adcomputer -identity UTW -properties * | select -property description

description
-----------
i_authenticate
```

Password: i_authenticate_things

## Century 13

```powershell
PS C:\users\century13\desktop> get-content -delimiter " " .\countmywords | Measure-Object


Count    : 755
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

## Century 14

```powershell
PS C:\users\century14\desktop> (select-string -path .\countpolos -pattern " polo" -allmatches).matches.count
153
```

## Century 15

Congratulations!

You have successfully made it to the end!

Try your luck with other games brought to you by the Under The Wire team.

Thanks for playing!
