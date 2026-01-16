while($true)
{
    Add-Type -AssemblyName PresentationCore,PresentationFramework
    $ButtonType = [System.Windows.MessageBoxButton]::YesNo
    $MessageboxTitle = "Reminder System"
    $Messageboxbody = "Are you still working?"
    $MessageIcon = [System.Windows.MessageBoxImage]::Warning
    
    $Result = [System.Windows.MessageBox]::Show($Messageboxbody,$MessageboxTitle,$ButtonType,$MessageIcon)

    if ($Result -eq "Yes") {
        Add-Type -AssemblyName Microsoft.VisualBasic
        $Working = [Microsoft.VisualBasic.Interaction]::InputBox("What are you working on?", "Reminder System")

        python "path\to\file\"workupdater.py $Working
    } else {
        $MessageboxTitle = "Reminder System"
        $Messageboxbody = "Understood."
        $MessageIcon = [System.Windows.MessageBoxImage]::Information
        [System.Windows.MessageBox]::Show($Messageboxbody,$MessageboxTitle)

        python "path\to\file\"dmlocator.py
    }

    Start-Sleep 420 # Sends a reminder every 7 minutes.
}