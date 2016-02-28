import unittest
import sys
sys.path.append('../vixen')
from vixen import Vixen
import VixenBaseTest
import os

class VixenFileTest(unittest.TestCase):
    vixen = None

    def suite():
        suite = unittest.TestLoader().loadTestsFromTestCase(VixenFileTest)
        return suite

    #@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")        
    def test_LoadWindowsPath(self):
        test1 = Vixen()
        vixfilename = "../VixenFiles/Sequences/Arduino6ChannelThisIsHolloweenMain.vix"
        print os.path.exists(vixfilename)
        test1.loadfile(vixfilename)
        self.assertEqual(test1.periods,0,'periods did not match file')
    
    @unittest.skip('Music Files are not present')
    def test_LoadMusicFile(self):
        vix = Vixen()
        musfile = '..\\VixenFiles\\Music\\03 - This Is Halloween.ogg'
        self.assertTrue(os.path.exists(musfile),'Audio File is missing from filesystem')
        vix.loadmusic(musfile)
        #print test2.value(0,100)
        #test2.play()
        while True:
            for per in range(vix.periods):
                print vix.musicfilename
                print vix.period(per)
                vix.pos_syncwait(per)
            else:
                break;

    def test_LoadXMLFile(self):
        test3 = Vixen()
        rootdir = os.path.dirname(os.path.realpath(__file__))
        SequencePath = os.path.join(rootdir,os.path.join("VixenFiles",os.path.join("Sequences","*.vix")))
        SequencePath = "..\\VixenFiles\\Sequences\\"
        print SequencePath
        for file in os.listdir(SequencePath):
            if(file[-3:]) == "vix":
                print file,
                print test3.channels
        self.assertRaises(IndexError,test3.loadfile,os.path.join(SequencePath,file))

    def test_VixFilePluginDataIsPresent(self):
        vixfilename = "../VixenFiles/Sequences/Arduino6ChannelThisIsHolloweenMain.vix"
        test3 = Vixen()
        test3.loadfile(vixfilename)
        test3.pluginData
        self.assertEqual(1,2,'not')
        

    def test_VixFilePluginDataIsNotPresent(self):
        test3 = Vixen()
        SequencePath = "../VixenFiles/Sequences/PythonDecodeSample2.vix"
        #test3.loadfile(SequencePath)
        self.assertRaises(IndexError,test3.loadfile,SequencePath)
  
    @unittest.skip("working on other tests")
    def test_PlayVixFileToEnd(self):
        test3 = Vixen()
        #rootdir = os.path.dirname(os.path.realpath(__file__))
        #SequencePath = os.path.join(rootdir,os.path.join("VixenFiles",os.path.join("Sequences","*.vix")))
        SequencePath = "../VixenFiles/Sequences/PythonDecodeSample2.vix"
        test3.loadfile(SequencePath)
        #print test3.channels


if __name__ == '__main__':
    unittest.main()