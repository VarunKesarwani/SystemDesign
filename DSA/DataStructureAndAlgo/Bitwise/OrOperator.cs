using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataStructureAndAlgo.Bitwise
{
    public class OrOperator
    {
        public static void Example()
        {
            uint a = 0b_1111_1000;
            uint b = 0b_1001_1101;
            uint c = a | b;
            Console.WriteLine(Convert.ToString(c, toBase: 2));
            Console.WriteLine(Convert.ToString(c, toBase: 10));
            // Output:
            // 1111 1101
        }
    }
}
