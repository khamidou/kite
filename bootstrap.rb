#!/usr/bin/env ruby
# Setup kite on a non-vagrant machine, like a digital ocean server
#
# This script goes through the following steps
# - setup ssh key-based auth on server
# - rsync the sources
# - run puppet on the server
 
if ARGV.length != 1 then
    puts "usage: $0 hostname"
    exit
end

hostname=ARGV[0]

if !ENV["SSH_AGENT_PID"] then 
    `ssh-add`
end

def exec_command(command)
    out = `#{command}`
    if !$?.success? then
        puts "FAIL.\n An error happened executing #{command}"
        puts "Output: #{out}"
    else
        puts "OK."
    end
end

printf "Setting up public key auth on #{hostname}: "
exec_command("ssh-copy-id root@#{hostname}")

printf "Setting up puppet: "
exec_command("ssh root@#{hostname} bash -c \"apt-get update && apt-get install -y rsync puppet\"")

printf "Copying the sources: "
exec_command("rsync -a -f\"- .git/\" ../kite root@#{hostname}:/root/")

puts "Applying Puppet configuration (this may take some time): "
exec_command("ssh root@#{hostname} bash -c \"puppet apply /root/kite/manifests/server.pp --modulepath=/root/kite/puppet_modules/\"")
