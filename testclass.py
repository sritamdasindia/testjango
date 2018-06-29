

class test:
    s =45
    def nsmethos( self ):
        print 'i am non static method '
        print self.s

    @classmethod
    def cmethod( cname ):
        print 'i am class method '
        print cname.s

    @staticmethod
    def smethod():
        print 'i am static method'
        print test.s

def main():
    test2 = test()
    print test . smethod
    test . cmethod()
    test2.cmethod()
    test2.nsmethos()

main()
