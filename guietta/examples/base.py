# -*- coding: utf-8 -*-

from guietta import B, E, _, Gui, Quit


gui = Gui(
    
  [  'Enter expression:', '__expr__'  , B('Eval!') ],
  [  'Result:'          , 'result'    , _          ],
  [  _                  , _           , Quit       ] )

gui.run()


    