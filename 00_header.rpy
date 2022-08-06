init -990 python in mas_submod_utils:
    Submod(
        author="otter",
        name="MAS Yandere Submod",
        description="Making Monika yandere, giving the player an experience of a toxic relationship as seen in the anime trope.",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Yandere Submod",
            user_name="my-otter-self",
            repository_name="mas_yandere",
            submod_dir="/Submods/MAS Yandere Submod",
            extraction_depth=3,
            redirected_files=(
                "README.md",
                "LICENSE.txt"
            )
        )
