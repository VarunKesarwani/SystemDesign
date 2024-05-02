using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices.Marshalling;
using System.Text;
using System.Threading.Tasks;

namespace DataStructureAndAlgo.Bitwise
{
    public class Conversation
    {
        public static uint BinaryToDecimal(int input)
        {
            var result = Convert.ToString(input, toBase: 2);
            return uint.Parse(result);
        }
        public static string DecimalToBinary(uint input)
        {
            return Convert.ToString(input, toBase: 10);
        }
    }
}
