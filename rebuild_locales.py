from pathlib import Path
import os
import shutil

#All mods to copy locales from
mods = {
    "omnilib",
    "omnimatter",
    "omnimatter_compression",
    "omnimatter_crystal",
    "omnimatter_energy",
    "omnimatter_fluid",
    "omnimatter_move",
    "omnimatter_permutation",
    "omnimatter_science",
    "omnimatter_water",
    "omnimatter_wood"
}

#OmniLocales repo path
locale_repo = Path(os.path.dirname(os.path.realpath(__file__)))
#Omnimatter repo path
omni_repo = locale_repo.parent/"omnimatter"


#Copy all en files to the locale repo
print("\n##Copying over en files to the locale repo...\n")
for modname in mods:
    filename = modname + ".cfg"
    #Copy current en files into the locales repo
    source_path = omni_repo/modname/"locale"/"en"
    dest_path = locale_repo/"locale"/"en"
    for obj in source_path.iterdir():
        if obj.is_file():
            os.makedirs(dest_path, exist_ok=True)
            shutil.copy(source_path/obj.name, dest_path/obj.name)
            print("Copied " + str(source_path/obj.name)+ " to " + str(dest_path/obj.name))


#Copy all translated files back into the omni dir
print("\n##Copying over translated files to the omni repo...\n")
source_lang_path = locale_repo/"locale"
for lang in source_lang_path.iterdir():
    #Dont copy en files back!!!
    if lang.name != "en":
        for obj in (source_lang_path/lang.name).iterdir():
            modname = obj.name.split(".")[0]
            #Check if the mod is on the whitelist before copying
            if (modname in mods):
                dest_path = omni_repo/modname/"locale"/lang.name
                #Create the language folder if it doesnt exist yet
                os.makedirs(dest_path, exist_ok=True)
                #copy files over
                shutil.copy(source_lang_path/lang.name/obj.name, dest_path/obj.name)
                print("Copied " + str(source_lang_path/lang.name/obj.name)+" to " + str(dest_path/obj.name))


print("Press enter to exit")
input()