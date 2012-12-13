
rem
rem image creation
rem   Use a CentOS a base image
rem     (build & install LSST software in the persistent disk)
rem   construct the .bashrc for the user account /opt/user
rem     setup lsst
rem   prepare contextualization scripts
rem     /usr/bin/stratuslab_lsst.context
rem     /etc/stratuslab/conf.d/50_lsst.context
rem        -> mount
rem   Configure the user account to be the default account
rem 
rem \install\stratuslab\windows\stratus-run-instance.bat --save --type m1.xlarge --comment "LSST" --vm-name=LSST --author "Christian Arnault" --author-email arnault@lal.in2p3.fr --image-version=2.0 --persistent-disk=4916226d-111b-490d-82ad-3f4d345ef65c Jd3yRF6x4ofxfCeVK6BmCkuHc0m

\install\stratuslab\windows\stratus-run-instance.bat --type m1.xlarge --comment "LSST" --vm-name=LSST --author "Christian Arnault" --author-email arnault@lal.in2p3.fr --image-version=2.0 --persistent-disk=4916226d-111b-490d-82ad-3f4d345ef65c I0LUGjx0HtEhimGgJXxrcfz9Y9J 


