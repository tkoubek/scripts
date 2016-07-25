#!/bin/bash

#sudo apt-get install -qqy ethtool libgraph-easy-perl graphviz > /dev/null
export PERL_MM_USE_DEFAULT=1
perl -MCPAN -e 'install Graph::Easy'
zypper --non-interactive --no-gpg-checks --quiet install --auto-agree-with-licenses ethtool graphviz openvswitch-switch



EXCEPT=/tmp/exceptlist
echo '' > $EXCEPT
result=""

function on_exit() {
  rm -f $EXCEPT
}

trap "on_exit" EXIT

# find ovs br <-> port
if [ "x$(which ovs-vsctl)" != "x" ]; then
  for br in $(sudo ovs-vsctl list-br); do
    for port in $(sudo ovs-vsctl list-ports $br); do
      result=$(echo "$result [$port]---->[$br] [$br]---->[$port] ")
    done
  done
fi

# find br <-> port
for br in $(brctl show | sed '1d' | grep '^[a-z]' | awk '{print $1}'); do
  for port in $(brctl show $br | sed '1d' | sed 's/.*\t.*\t.*\t\(.*\)/\1/g'); do
    result=$(echo "$result [$port]---->[$br] [$br]---->[$port] ")
  done
done

# ip namespace veth
for ns in $(ip netns); do
  for interface in $(ip netns exec $ns ip a | cut -d':' -f-2 | grep ^[1-9]); do
    index=$(ip netns exec $ns ethtool -S $interface 2> /dev/null | grep peer_ifindex | awk '{print $2}')
    ifname=$(ip netns exec $ns ip a | grep "^$index:" | awk '{print $2}' | cut -d':' -f1)
    if [ "x$ifname" == "x" ]; then
      ifname=$(ip a | grep "^$index:" | awk '{print $2}' | cut -d':' -f1)
      if [ "x$ifname" != "x" ]; then
        echo $ifname >> $EXCEPT
        result=$(echo "$result [$interface]---->[$ifname] [$ifname]---->[$interface] ")
      fi
    fi
  done
done

# ip veth
for interface in $(ip a | cut -d':' -f-2 | grep ^[1-9]); do
  if cat $EXCEPT | grep -q "^$interface$" ; then continue ; fi
  index=$(ethtool -S $interface 2> /dev/null | grep peer_ifindex | awk '{print $2}')
  ifname=$(ip a | grep "^$index:" | awk '{print $2}' | cut -d':' -f1)
  if [ "x$ifname" != "x" ]; then
    echo $ifname >> $EXCEPT
    result=$(echo "$result [$interface]---->[$ifname] [$ifname]---->[$interface] ")
  fi
done

# vm tap
for tap in $(ip a | cut -d':' -f-2 | grep ^[1-9]  | cut -d' ' -f2 | grep '^tap'); do
  vmuuid=$(grep -rl "$tap" /var/lib/nova/instances/*/libvirt.xml | cut -d'/' -f6)
  if [ "x$vmuuid" != "x" ]; then
    result=$(echo "$result [$tap]---->[VM-$vmuuid] [VM-$vmuuid]---->[$tap] ")
  fi
done

rm -f $EXCEPT

echo $result | graph-easy
echo $result | graph-easy -as dot | dot -Tpng -o l2path.png
