#!/usr/bin/env ruby

=begin
Finds the pythagorean triplet for which a+b+c = 1000.

A pythagorean triplet is a set of natural numbers, a < b < c such that a**2 + b**2 = c**2.
=end

def is_pythagorean_triplet?(a,b,c)
  a**2 + b**2 == c**2 
end

(1..1000).each do |i|
  (i..1000).each do |j|
    (j..1000).each do |k|
      if i+j+k == 1000 and is_pythagorean_triplet?(i,j,k)
        puts "i: #{i} j: #{j} k: #{k}"
        puts "i*j*k: #{i*j*k}"
        return
      end
    end
  end
end
