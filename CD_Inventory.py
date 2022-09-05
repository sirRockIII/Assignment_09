#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# COsuji, 2022-Sep-04,  Modified code to handle errors from input, type casting, etc
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO
#import DataClasses as DC


lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        try:
            tplCdInfo = IO.ScreenIO.get_CD_info()
            PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        except:
            print('Invalid ID entry')
        else:
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        try:
            cd_idx = int(input('Select the CD / Album index: '))
        except:
            print("CD / Album index must be an integer")
            continue
        else:
            try:
                cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
            except:
                print("CD / Album index does not exist")
                continue
       
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                break
            if strChoice == 'a':
               try: 
                   tplTrkInfo = IO.ScreenIO.get_track_info()
                   PC.DataProcessor.add_track(tplTrkInfo, cd)
               except:
                    print("Invalid Track position. Ensure poition is an Interger")
                    continue
            
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'r':
                
                try:
                    IO.ScreenIO.show_tracks(cd)
                    trk_idx = int(input('Select the Track index: '))
                except:
                    print('Please enter an integer')
                    continue
                else:
                    cd.rmv_track(trk_idx)
            else:
                print('General Error')
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')