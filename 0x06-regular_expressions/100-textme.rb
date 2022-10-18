#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\S+\w)\W+to:(\S+\w)\W+flags:(\S+\w)/).join(",")
