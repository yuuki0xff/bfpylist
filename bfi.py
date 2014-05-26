#!/usr/bin/env python2
# coding: utf8

import sys

##############################
# sample code

#code=sys.stdin.read()
#code='+++++++++[>++++++++>+++++++++++>+++++<<<-]>.>++.+++++++..+++.>-.------------.<++++++++.--------.+++.------.--------.>+.' #Hello, world!
#code='++++++[->++++> >+>+>-<<<<<]>[<++++> >+++>++++> >+++>+ ++++>+++++> > > > > >++> >++<<<<<<<<<<<<<<-]<++++>+++ >-->+++>-> >--->++> > >+++++[->++>++<<]<<<<<<<<<<[->- [> > > > > > >]>[<+++>.>.> > > >..> > >+<]<<<<<-[> > > >]>[<+ ++++>.>.>..> > >+<]> > > >+<-[<<<]<[[-<<+> >]> > >+>+<<<<< <[-> >+>+>-<<<<]<]>>[[-]<]>[> > >[>.<<.<<<]<[.<<<<]>]>.<<<< <<<<<<<] ' #Fizz Buzz
#code='+[>,.<]' #echo


il=[0] #index list # ループの継続に使用する
lsi=[] #loop start index
skip=[0]

cs=list(code)
mem=[[0]]
p=[0]

[
	(
		skip[0]!=0 and (
			(cs[ind]=='[' and (skip.append(skip.pop()+1) or True)) or
			(cs[ind]==']' and (skip.append(skip.pop()-1) or True)) or
			True
		) or skip[0]==0 and (
			(cs[ind]==' ' or cs[ind]=='\n' or cs[ind]=='\r') or

			(cs[ind]=='.' and (sys.stdout.write(chr(mem[p[0]][0])) or True)) or
			(cs[ind]==',' and (
				( mem[p[0]].pop() or True ) and
				( mem[p[0]].append(ord(sys.stdin.read(1)))) or True)) or

			(cs[ind]=='+' and (mem[p[0]].append(mem[p[0]].pop()+1) or True)) or
			(cs[ind]=='-' and (mem[p[0]].append(mem[p[0]].pop()-1) or True)) or

			(cs[ind]=='<' and (p.append(p.pop()-1) or True)) or
			(cs[ind]=='>' and (
				( (len(mem)-1)<=p[0] and mem.append([0]) or True ) 
				and p.append(p.pop()+1) or True)) or

			(cs[ind]=='[' and mem[p[0]][0]!=0 and (lsi.append(ind) or True)) or
			(cs[ind]=='[' and (skip.append(skip.pop()+1) or True)) or
			(cs[ind]==']' and (il.append(lsi.pop()) or False)) or
			False
		)
	) and
		len(cs)-1>ind and il.append(il[len(il)-1]+1)
for ind in il ] and None
#############
#il
#lsi
#skip
#mem
#p

