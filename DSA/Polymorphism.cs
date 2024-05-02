namespace VirtualMethod
{
    public abstract class Felidae
    {
        private bool male;
        // This constructor calls another constructor
        public Felidae() : this(true)
        { }
        // This is the constructor that is inherited
        public Felidae(bool male)
        {
            this.male = male;
        }
        public bool Male
        {

            get { return male; }
            set { this.male = value; }
        }
        public abstract void CatchPrey(object prey);
        public abstract String GetTypicalSound();
    }

    public interface Reproducible<T> where T : Felidae
    {
        T[] Reproduce(T mate);
    }

    public class Lion : Felidae, Reproducible<Lion>
    {
        private int weight;
        // Keyword "base" will be explained in the next paragraph
        public Lion(bool male, int weight) : base(male)
        {
            this.weight = weight;
        }
        public int Weight
        {
            get { return weight; }
            set { this.weight = value; }
        }
        public override void CatchPrey(object prey)
        {
            Console.WriteLine("Lion.CatchPrey");
        }

        Lion[] Reproducible<Lion>.Reproduce(Lion mate)
        {
            return new Lion[] { new Lion(true, 12), new Lion(false, 10) };
        }
        public sealed override string GetTypicalSound()
        {
            return "Roar!";
        }

    }

    public class AfricanLion : Lion
    {
        public override void CatchPrey(object prey)
        {
            Console.WriteLine("AfricanLion.CatchPrey");
        }

        //protected override string GetTypicalSound()
        //{
        //    return "High Roar!";
        //}

        public AfricanLion(bool male, int weight) : base(male, weight)
        {
        }
    }
    public class IndiaLion : Lion
    {
        public IndiaLion(bool male, int weight) : base(male, weight)
        {
        }

        public override void CatchPrey(object prey)
        {
            Console.WriteLine("IndiaLion.CatchPrey");
            Console.WriteLine("calling base.CatchPrey");
            Console.Write("\t");
            base.CatchPrey(prey);
            Console.WriteLine("...end of call.");
        }
        //protected override string GetTypicalSound()
        //{
        //    return "Low Roar!";
        //}
    }
    internal class Polymorphism
    {
        public static void Example()
        {
            Lion lion = new Lion(true, 80);
            lion.CatchPrey(null);
            // Will print "Lion.CatchPrey"

            AfricanLion Alion = new AfricanLion(true, 120);
            Alion.CatchPrey(null);
            // Will print "AfricanLion.CatchPrey"

            Lion ALlion = new AfricanLion(false, 60);
            ALlion.CatchPrey(null);
            Console.WriteLine(ALlion.GetTypicalSound());
            
            // Will print "AfricanLion.CatchPrey", because
            // the variable lion has a value of type AfricanLion
            // the implementation of the base class is hidden and omitted.

            Lion ILlion = new IndiaLion(false, 60);
            ILlion.CatchPrey(null);
            Console.WriteLine(ILlion.GetTypicalSound());
            //IndiaLion.CatchPrey
            //calling base.CatchPrey
            //Lion.CatchPrey
            //It has called the base class implementation, using base keyword.

        }

    }
}
