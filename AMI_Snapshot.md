# Instance :
   - An EC2 instance is similar to a server where you can host your websites or applications to make it available Globally.
   - You can increase or decrease the capacity of these instances as per the requirements.
   - It is highly scalable and works on pay-as-you-go model.
   
# AMI :
   - AMI provides the information required to launch the EC2 instance.
   - Users can launch multiple instances with the same configuration from a single AMI.
   - AMI includes the pre-configured templates of the operating system that runs on the AWS.
   
# Snapshot :
   - Snapshots are the incremental backups for the Amazon EBS.
   - Data in the EBS are stored in S3 by taking point-to-time snapshots.
   - Multiple EBS can be created using these snapshots
   - Unique data’s are only deleted, when a snapshot is deleted
   
## in simple word snapshot is : 
    Snapshots are not backups, and VMware does not support them in this capacity. They are 
    temporary restore points in time that allow for quickly reverting an entire virtual machine,
    including its settings, to its previous state at a specific point in time. Snapshots can be
    useful in development environments providing a quick rollback mechanism to test processes, 
    patches, settings, etc. VMware snapshots work in a “chain”, meaning that they require and 
    rely on the base VMDK disks and any other delta disks in place to reflect the current virtual
    machine state. Thus, if any disk in the chain is corrupted, the whole chain becomes corrupt. 
    In contrast, using backups provides an autonomous way to preserve and restore your data, 
    without relying on either the physical infrastructure or underlying virtual disks. So, 
    never use snapshots instead of backups !!
