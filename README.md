# SummerCampSHiFT
A modification of "Friday the 13th: The Game" for SHiFT and his community.

## Installing

### NEW PAK METHOD
Video Tutorial: N/A

If you have already installed the mod using the [old method](#old-loose-files-method) in the past, then first complete one of the two below before continuing:

**OPTION A - Reinstall Friday (Recommended):**
1. Uninstall through Steam
2. Delete the `F13Game` folder manually
3. Reinstall through Steam

**OPTION B - Disable the Old Method:**
1. Make sure you still have `quickbms-friday`
2. Drag `EAC_Launcher.exe` into `Disable-Mods.bat`
3. It should say that mod loading has been disabled (You will NOT need to re-enable it later)

**If you are already on a fresh install, or you have completed one of the two options above, you are now ready to begin!**

1. Open this link: https://github.com/AaronRules5/SummerCampSHiFT/releases
2. View the most recent release, open the `Assets` dropdown, and download `SCSHiFT-v#.#-Pak.zip`
3. Go to Friday the 13th: The Game in your Steam library
4. Click the ⚙, and go to Manage > Browse local files
5. Copy everything inside of the ZIP file you downloaded into this folder
6. You're done! Try it out!

---

### OLD LOOSE FILES METHOD
Video Tutorial: https://www.youtube.com/watch?v=qyHfHogSmXE \
**WARNING: CONFIRM THE DEVICE FRIDAY'S INSTALLED ON HAS AT LEAST ~20 GB OF FREE STORAGE BEFORE CONTINUING**

1. Open this link: https://github.com/AaronRules5/SummerCampSHiFT/releases
2. View the most recent release, open the `Assets` dropdown, download `quickbms-friday.zip` and `SCSHiFT-v#.#-Loose.zip`
3. Extract the contents of `quickbms-friday.zip` into a folder named `quickbms-friday`
4. Go to Friday the 13th: The Game in your Steam library
5. Click the ⚙, and go to Manage > Browse local files
6. Drag `EAC_Launcher.exe` from Friday's local files into the `Extract-Friday-Assets.bat` inside `quickbms-friday`
7. Press any key to begin extraction. This process should take around 30 minutes to complete
8. Copy the `SummerCamp` folder that's inside `SCSHiFT-v#.#-Loose.zip` into the same directory where `EAC_Launcher.exe` resides
   - (You're overwriting the original SummerCamp folder that's already there)
10. You're DONE! Mod loading is enabled by default. If you would like to disable or re-enable mod loading, drag `EAC_Launcher.exe` into `Disable-Mods.bat` or `Enable-Mods.bat`

## Contributing

Do **NOT** push binary Unreal files (.UASSET, .UEXP, .UBULK, .LOCRES, etc.) to the repository!\
Only upload easily editable files such as .WAV, .BLEND, .TXT, etc.\
They will be compiled into formats compatible with Friday and provided in a Release zip by Aaron.
