#!/usr/bin/env ruby

=begin
Finds the largest palindrome that is the product of two three-digit numbers.
=end

class String
  def is_palindrome
    if self.length == 0 or self.length == 1 then
      return true
    elsif self[0] != self[-1]
      return false
    else 
      return self[1..-2].is_palindrome
    end
  end
end

max = 0
(100..999).each do |i|
  (i..999).each do |j|
    p = i*j
    if p > max and p.to_s.is_palindrome
      max = p 
    end
  end
end
puts max
