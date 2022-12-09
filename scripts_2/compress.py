import os
import sys
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet
from PDFNetPython import *


def compress_file(input_filename):
    # Relative path to the folder containing the test files.
    input_path = "Z:/PgX/PDF/uncompressed/"
    output_path = "Z:/PgX/PDF/"
    Output_path2 = "W:/MEDNAWISEREPORTS/"

    PDFNet.Initialize("demo:1653194539225:7b869496030000000070ac906c64018164e427f1ece67e4078c9e88c34")
    doc = PDFDoc(input_path + input_filename + ".pdf")
    doc.InitSecurityHandler()
    Optimizer.Optimize(doc)
    doc.Save(output_path + input_filename + ".pdf", SDFDoc.e_linearized)
    doc.Save(Output_path2 + input_filename + ".pdf", SDFDoc.e_linearized)
    doc.Close()
