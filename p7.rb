#!/usr/bin/env ruby

=begin
Find the 100001st prime.
=end

require 'Prime'
puts Prime.take(10001)[-1]
