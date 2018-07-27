$::disks.keys.each |$disk| {
    if $disk !~ /sda/ {
        file { "/sys/class/block/${disk}/queue/read_ahead_kb":
            content     =>  "8",
            backup      =>  false
        }
    }
}