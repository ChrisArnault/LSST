#!/bin/bash -x

rm -f /lib/udev/rules.d/*net-gen*
rm -f /etc/udev/rules.d/*net.rules

fdisk -l

mkdir /opt/lsst
mount /dev/sdc /opt/lsst

adduser -d /opt/lsst lsst
adduser -d /opt/user user

ls -ls /opt/lsst

yum install -y gcc-c++ gcc-gfortran flex bison libXt-devel ncurses-devel readline-devel libuuid-devel zlib-devel bzip2-devel perl make

export NCORES=$((sysctl -n hw.ncpu || (test -r /proc/cpuinfo && grep processor /proc/cpuinfo | wc -l) || echo 2) 2>/dev/null)

cat > /opt/user/.bashrc <<EOF
#!/bin/bash -x
unset LSST_HOME EUPS_PATH LSST_DEVEL

export NCORES=$((sysctl -n hw.ncpu || (test -r /proc/cpuinfo && grep processor /proc/cpuinfo | wc -l) || echo 2) 2>/dev/null)
export MAKEFLAGS="-j $NCORES"
export SCONSFLAGS="-j $NCORES"

cd /opt/lsst
source /opt/lsst/eups/default/bin/setups.sh
setup lssteups
source /opt/lsst/loadLSST.sh

EOF


