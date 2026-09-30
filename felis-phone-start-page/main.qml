import QtQuick 2.6
import Sailfish.Silica 1.0
import Nemo.Configuration 1.0

Page {
    id: page

    ConfigurationValue {
        id: startPageConfig
        key: "/feliscatus/phone/startPage"
        defaultValue: 0
    }

    SilicaFlickable {
        anchors.fill: parent
        contentHeight: contentColumn.height

        Column {
            id: contentColumn
            width: parent.width

            PageHeader {
                title: "Phone Start Page"
            }

            ComboBox {
                width: parent.width
                label: "Default page"
                currentIndex: Math.max(0, Math.min(2, Number(startPageConfig.value)))

                menu: ContextMenu {
                    MenuItem { text: "Dialer" }
                    MenuItem { text: "History" }
                    MenuItem { text: "Contacts" }
                }

                onCurrentIndexChanged: {
                    if (currentIndex >= 0 && currentIndex <= 2 && Number(startPageConfig.value) !== currentIndex) {
                        startPageConfig.value = currentIndex
                    }
                }
            }

            Label {
                x: Theme.horizontalPageMargin
                width: parent.width - 2 * Theme.horizontalPageMargin
                wrapMode: Text.Wrap
                color: Theme.secondaryColor
                text: "Select which tab is shown when the Phone application opens."
            }
        }
    }
}
