using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataStructureAndAlgo.Bitwise
{
    public class NotOperator
    {
        public static void Example()
        {
            //this is a unary operator, which means that it is applied to a single operand
            uint a = 0b_0000_1110;
            uint c = ~a;
            Console.WriteLine(Convert.ToString(c, toBase: 2));
            Console.WriteLine(Convert.ToString(c, toBase: 10));
            // Output:
            // 1111_0001
        }
    }
}
