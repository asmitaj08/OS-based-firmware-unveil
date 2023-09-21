# Unveil OS-based IoT firmware

N.B. It's currently for linux based firmwares. Given the firmware binary, it extracts the firmware using binwalk, displays the correspoding file system. uses firmwalker to identify the sensitive files, and uses cve-bin-tool to display the softwrae component with existing CVEs.
## Targeting Features
* Firmware Extraction
* Extracted file traversal/listing
* Software componenet version identification and corresponding CVE finding
