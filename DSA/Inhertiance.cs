using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VirtualMethod
{
    class BaseClass
    {
        public virtual void Method1()
        {
            Console.WriteLine("Base - Method1");
        }
        public void Method2()
        {
            Console.WriteLine("Base - Method2");
        }

        public void Method3()
        {
            Console.WriteLine("Base - Method3");
        }
    }

    class DerivedClass : BaseClass
    {
        public override void Method1()
        {
            Console.WriteLine("Derived - Method1");
        }
        public new void Method2()
        {
            Console.WriteLine("Derived - Method2");
        }
        public void Method3()
        {
            Console.WriteLine("Base - Method3");
        }
    }
    internal class Inhertiance
    {
        public static void Example()
        {
            // The following two calls do what you would expect. They call  
            // the methods that are defined in BaseClass. 
            BaseClass bc = new BaseClass();
            bc.Method1();
            bc.Method2();
            bc.Method3();
            //Base - Method1
            //Base - Method2
            //Base - Method3

            // The following two calls do what you would expect. They call  
            // the methods that are defined in DerivedClass.  
            DerivedClass dc = new DerivedClass();
            dc.Method1();
            dc.Method2();
            dc.Method3();
            //Derived - Method1
            //Derived - Method2
            //Base - Method3

            // The following two calls produce different results, depending
            // on whether override (Method1) or new (Method2) is used. 
            BaseClass bcdc = new DerivedClass();
            bcdc.Method1();
            bcdc.Method2();
            bcdc.Method3();
            //Derived - Method1 //override
            //Base - Method2 // new
            //Base - Method3


            // Error
            //DerivedClass dcbc = new BaseClass();
        }

    }
}
