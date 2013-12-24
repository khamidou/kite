#!/usr/bin/env ruby
# Setup kite on a non-vagrant machine, like a digital ocean server
#
# This script goes through the following steps
# - setup ssh key-based auth on server
# - setup git and puppet
# - clone the kite sources from github
# - run puppet on the server
 
if ARGV.length != 1 then
    puts "usage: $0 hostname"
    exit
end

hostname=ARGV[0]

if !ENV["SSH_AGENT_PID"] then 
    `ssh-add`
end

printf "Setting up public key auth on #{hostname} "
`ssh-copy-id root@#{hostname}`
puts "OK"

srcrepo = "https://github.com/khamidou/kite.git"
printf "Getting the sources from #{srcrepo} "

`ssh root@#{hostname} bash -c "\
apt-get update;\
apt-get install -y git puppet;\
git clone #{srcrepo} /root/kite;"`

puts "OK"
