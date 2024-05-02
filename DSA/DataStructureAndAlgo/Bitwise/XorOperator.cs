using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataStructureAndAlgo.Bitwise
{
    public class XorOperator
    {
        public static void Example()
        {
            uint a = 0b_0000_1110;
            uint b = 0b_0000_1011;
            uint c = a ^ b;
            Console.WriteLine(Convert.ToString(c, toBase: 2));
            Console.WriteLine(Convert.ToString(c, toBase: 10));
            // Output:
            // 0000_0101
        }
    }
}
