//to read and write to text file from the ACE software 4.7

using Ace.Services.NameLookup;
using Ace.Server;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

namespace Ace.Custom {

	public class Program : IDisposable {

		public INameLookupService ace;

		public void Main () {
			
			
			
			string filePath = @"C:\Users\prath\Desktop\example.txt";  // Change the path as needed

			Trace.WriteLine("Script Starting");
			string createText = "Hello and Welcome" + Environment.NewLine;
			File.WriteAllText(filePath, createText);

        try
        {
            // Read all lines from the file and display them
            string[] lines = File.ReadAllLines(filePath);

            // Print each line
            foreach (string line in lines)
            {
                Console.WriteLine(line);
            }
        }
        catch (FileNotFoundException e)
        {
            Console.WriteLine($"The file was not found: '{e}'");
        }
        catch (IOException e)
        {
            Console.WriteLine($"An I/O error occurred: '{e}'");
        }
			
		}

		public void Dispose () {
			
		}
	}
}