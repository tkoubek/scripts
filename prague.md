# Prague QA cloud infrastructure

## IPMI access


### Cloud servers
| Node     | IP             | IPMI Mac adress   |
|----------|----------------|-------------------|
| kronos   | 10.100.103.197 | 0C:C4:7A:6E:68:81 |
| leto     | 10.100.103.213 | 0C:C4:7A:AE:7E:02 |
| thebe    | 10.100.103.201 | 0C:C4:7A:AE:7C:9F |
| europa   | 10.100.103.202 | 0C:C4:7A:AE:C6:6A |
| erlara   | 10.100.103.196 | 0C:C4:7A:6E:68:82 |
| carpo    | 10.100.103.200 | 0C:C4:7A:AE:7E:AB |
| hersi    | 10.100.103.203 | 0C:C4:7A:AE:CA:4A |
| sponde   | 10.100.103.247 | 0C:C4:7A:AE:77:2E |
| zeus     | 10.100.103.167 | 0C:C4:7A:7C:DF:2A |
| themisto | 10.100.103.199 | 0C:C4:7A:AE:7D:D2 |

### Storage servers
| Node     | IP             | IPMI Mac adress   |
|----------|----------------|-------------------|
| callisto | 10.100.103.222 | 0c:c4:7a:7c:DE:f1 |
| artemis  | 10.100.103.223 | 0c:c4:7a:7c:df:28 |
| poseidon | 10.100.103.224 | 0c:c4:7a:7d:ed:72 |
| hera     | 10.100.103.225 | 0C:C4:7A:7C:DF:05 |
| apollo   | 10.100.103.238 | 0C:C4:7A:7D:ED:B3 |
| ares     | 10.100.103.239 | 0C:C4:7A:7C:DF:19 |
| maia     | 10.100.103.240 | 0C:C4:7A:7C:DF:0B |
| demeter  | 10.100.103.241 | 0C:C4:7A:7C:DF:0A |


## Cloud server nodes

| Host     | FQDN hostname                | Mac address       | VLANs                     |
|----------|------------------------------|-------------------|---------------------------|
| zeus     | zeus.qa.suse.cz              | 0c:c4:7a:7c:e2:ea | 12(Untagged)              |
|          |                              | 0c:c4:7a:7c:e2:eb | 742(Untagged)             |
| themisto | 0c-c4-7a-aa-27-2c.qa.suse.cz | 0c:c4:7a:aa:27:2c | 742(Untagged),743,744,745 |
| thebe    | 0c-c4-7a-aa-45-dc.qa.suse.cz | 0c:c4:7a:aa:45:dc | 742(Untagged),743,744,745 |
| europa   | 0c-c4-7a-aa-d4-b0.qa.suse.cz | 0c:c4:7a:aa:d4:b0 | 742(Untagged),743,744,745 |
| erlara   | 0c-c4-7a-6c-40-e2.qa.suse.cz | 0c:c4:7a:6c:40:e2 | 742(Untagged),743,744,745 |
| carpo    | 0c-c4-7a-aa-45-82.qa.suse.cz | 0c:c4:7a:aa:45:82 | 742(Untagged),743,744,745 |
| hersi    | 0c-c4-7a-aa-d1-b4.qa.suse.cz | 0c:c4:7a:aa:45:82 | 742(Untagged),743,744,745 |
| sponde   | 0c-c4-7a-aa-47-64.qa.suse.cz | 0c:c4:7a:aa:47:64 | 742(Untagged),743,744,745 |
| kronos   | 0c-c4-7a-6c-40-e4.qa.suse.cz | 0c:c4:7a:6c:40:e4 | 742(Untagged),743,744,745 |
| leto     | 0c-c4-7a-aa-43-80.qa.suse.cz | 0c:c4:7a:aa:43:80 | 742(Untagged),743,744,745 |

## Storage server nodes

| Host     | FQDN hostname                | Mac address       | VLANs             |
|----------|------------------------------|-------------------|-------------------|
| apollo   | 0c-c4-7a-7d-f0-4c.qa.suse.cz | 0c:c4:7a:aa:43:80 | 742(Untagged),744 |
| poseidon | 0c-c4-7a-7d-ef-cb.qa.suse.cz | 0c-c4-7a-7d-ef-cb | 742(Untagged),744 |
| ares     | 0c-c4-7a-7c-e2-c8.qa.suse.cz | 0c-c4-7a-7c-e2-c8 | 742(Untagged),744 |
| artemis  | 0c-c4-7a-7c-e2-e6.qa.suse.cz | 0c-c4-7a-7c-e2-c8 | 742(Untagged),744 |
| demeter  | 0c-c4-7a-7c-e2-aa.qa.suse.cz | 0c-c4-7a-7c-e2-aa | 742(Untagged),744 |
| hera     | 0c-c4-7a-7c-e2-a0.qa.suse.cz | 0c-c4-7a-7c-e2-a0 | 742(Untagged),744 |
| maia     | 0c-c4-7a-7c-e2-ac.qa.suse.cz | 0c-c4-7a-7c-e2-ac | 742(Untagged),744 |
| callisto | 0c-c4-7a-7c-e2-78.qa.suse.cz | 0c-c4-7a-7c-e2-78 | 742(Untagged),744 |




## Cloud Switch C3SRV1-B-5 (Cisco SG300)

| port # | mode   | Host     | Description |
|--------|--------|----------|-------------|
| 1      | trunk  | leto     | Eth0        |
| 2      |        |          |             |
| 3      | access | kronos   | IPMI        |
| 4      | access | leto     | IPMI        |
| 5      | access | thebe    | IPMI        |
| 6      | access | europa   | IPMI        |
| 7      | access | erlara   | IPMI        |
| 8      | access | carpo    | IPMI        |
| 9      | access | hersi    | IPMI        |
| 10     | access | sponde   | IPMI        |
| 11     | access | zeus     | IPMI        |
| 12     |        |          | PBU         |
| 13     |        |          |             |
| 14     | trunk  | zeus     | Eth1        |
| 15     | access | themisto | IPMI        |
| 16     | trunk  | europa   | Eth0        |
| 17     | trunk  | kronos   | Eth0        |
| 18     | trunk  | themisto | Eth0        |
| 19     | access | zeus     | Eth0        |
| 20     | trunk  | sponde   | Eth0        |
| 21     | trunk  | hersi    | Eth0        |
| 22     | trunk  | erlara   | Eth0        |
| 23     | trunk  | carpo    | Eth0        |
| 24     | trunk  | thebe    | Eth0        |

## Storage Switch C3SRV1-B-4 (Cisco SG300)

| port # | mode   | Host     | Description |
|--------|--------|----------|-------------|
| 1      | access | ares     | IPMI        |
| 2      | access | apollo   | IPMI        |
| 3      | access | poseidon | IPMI        |
| 4      |        |          |             |
| 5      |        |          |             |
| 6      | access | artemis  | IPMI        |
| 7      | access | maia     | IPMI        |
| 8      | access | hera     | IPMI        |
| 9      | access | demetris | IPMI        |
| 10     | access | callisto | IPMI        |
| 11     | trunk  | poseidon | Eth0        |
| 12     | trunk  | apollo   | Eth0        |
| 13     |        |          |             |
| 14     |        |          |             |
| 15     |        |          |             |
| 16     |        |          |             |
| 17     |        |          |             |
| 18     |        |          |             |
| 19     | trunk  | callisto | Eth0        |
| 20     | trunk  | maia     | Eth0        |
| 21     | trunk  | hera     | Eth0        |
| 22     | trunk  | ares     | Eth0        |
| 23     | trunk  | artemis  | Eth0        |
| 24     | trunk  | demetris | Eth0        |


## VLANs

### Cloud

| VLAN id |                         VLAN Name                         | Type     |
|---------|-----------------------------------------------------------|----------|
| 12      | Prague QA Network                                         | Untagged |
| 712     | Spare I - qamagic (Used for Nova Floating Public Network) | Tagged   |
| 742     | Admin Network                                             | Untagged |
| 743     | Private Network (Nova Fixed)                              | Tagged   |
| 744     | Storage Network                                           | Tagged   |
| 745     | Software defined Network                                  | Tagged   |

### Storage

| VLAN id | VLAN Name         | Type     |
|---------|-------------------|----------|
| 12      | Prague QA Network | Untagged |
| 738     | Admin Network     | Untagged |
| 740     | Storage Network   | Tagged   |

## Hardware

### Cloud

| Host     | Server                   | Size | CPUs         | RAM       | Hard drives                 |
|----------|--------------------------|------|--------------|-----------|-----------------------------|
| zeus     | Intel Single-CPU RI1104H | 1U   | 1x Quad-Core | 32GB RAM  | 2x 240GB SSD                |
| themisto | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 64GB RAM  | 2x 240GB SSD                |
| thebe    | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 64GB RAM  | 2x 240GB SSD                |
| europa   | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 64GB RAM  | 2x 240GB SSD                |
| erlara   | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 128GB RAM | 1x 240GB SSD + 2x 960GB SSD |
| carpo    | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 128GB RAM | 1x 240GB SSD + 2x 960GB SSD |
| hersi    | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 128GB RAM | 1x 240GB SSD + 2x 960GB SSD |
| sponde   | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 128GB RAM | 1x 240GB SSD + 2x 960GB SSD |
| kronos   | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 128GB RAM | 1x 240GB SSD + 2x 960GB SSD |
| leto     | Intel Dual-CPU RI2104H   | 1U   | 2x Octa-Core | 128GB RAM | 1x 240GB SSD + 2x 960GB SSD |

### Storage

| Host     | Server                   | Size | CPUs         | RAM      | Hard Drives            |
|----------|--------------------------|------|--------------|----------|------------------------|
| apollo   | Intel Single-CPU RI1104H | 1U   | 1x Quad-Core | 32GB RAM | 2x 240GB SSD           |
| poseidon | Intel Single-CPU RI1104H | 1U   | 1x Quad-Core | 32GB RAM | 2x 240GB SSD           |
| ares     | Intel Single-CPU RI1208  | 2U   | 1x Quad-Core | 16GB RAM | 240GB SSD + 5x 2TB HDD |
| artemis  | Intel Single-CPU RI1209  | 2U   | 1x Quad-Core | 16GB RAM | 240GB SSD + 5x 2TB HDD |
| demeter  | Intel Single-CPU RI1210  | 2U   | 1x Quad-Core | 16GB RAM | 240GB SSD + 5x 2TB HDD |
| hera     | Intel Single-CPU RI1211  | 2U   | 1x Quad-Core | 16GB RAM | 240GB SSD + 5x 2TB HDD |
| maia     | Intel Single-CPU RI1212  | 2U   | 1x Quad-Core | 16GB RAM | 240GB SSD + 5x 2TB HDD |
| callisto | Intel Single-CPU RI1213  | 2U   | 1x Quad-Core | 16GB RAM | 240GB SSD + 5x 2TB HDD |
