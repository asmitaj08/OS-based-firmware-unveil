## Features for Linux OS based firmware analysis framework
### Binary extraction 
* Case 1 : Binary is not encrypted and can be extracted by binwalk - done
* Case 2 : Binary is not encrypted but binwalk doesn't give out proper result - pending
* Case 3 : Binary is encrypted (Currently not in scope but can be explored in future)

### Identifying CVEs w.r.t software components present in the firmware
* CVE lookup w.r.t. version number of the sofware component (drawback - it will not give correct result, if the patching of the software components is done without updating the version number)
    * Using pre-defined set of software components to look for, find version number and provide corresponding CVEs (Currently done using CVE-bin tool).
      Pending - This needs work to check the software components that are not covered by cve-bin tool, and implement corresponding checkers manually.
                Understand backened of cve-bin tool implementation.
    * Implement the cve lookup for all the software components present in the firmware (understand backened implementation of cve-search and combine with it the implementation of cve-bin tool)
* Implementation not just dependant on version number, but rather correlation with the already found vulnerability that is maintained in the database.
      
### Inclusion of emulation and fuzzing for finding implementation related bugs like RCE, memory leaks, XSS, memory corruption, malicious payload, etc (pending)

### Creating firmware database for better analysis (that would also be required for perfroming correlation , and also required for ML integration in this project in future)

### Framework UI - Pending