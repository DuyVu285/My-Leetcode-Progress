class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        main_folders = []
        for f in folder:
            if not main_folders or not f.startswith(main_folders[-1] + '/'):
                main_folders.append(f)
        return main_folders