module Catalog exposing (..)

import Domain exposing (..)
import Html exposing (Html, div, img, text, hr)
import Html.Attributes exposing (src, style, class)
import Material.Button as Button
import Material.Card as Card
import Material.Color as Color
import Material.Elevation as Elevation
import Material.Icon as Icon
import Material.Options as Options exposing (css, cs)
import Maybe
import Phrases exposing (..)


type CultivarCardRole
    = Primary
    | Secondary


cultivarById : Maybe CultivarId -> Model -> Maybe Cultivar
cultivarById id model =
    List.filter (\x -> Just x.id == id) model.cultivars |> List.head


imgUrl : Cultivar -> Url
imgUrl c =
    Maybe.withDefault "/img/generic-cultivar.png" c.imgUrl


maybeSelectedCultivar : Model -> Html Msg
maybeSelectedCultivar model =
    case cultivarById model.selectedCultivar model of
        Nothing ->
            emptyNode

        Just c ->
            selectedCultivarView model c


maybeSecondarySelection : Model -> Html Msg
maybeSecondarySelection model =
    case cultivarById model.secondarySelectedCultivar model of
        Nothing ->
            emptyNode

        Just c ->
            selectedCultivarCard model c Secondary


selectionBoxWidth : Model -> String
selectionBoxWidth model =
    case model.secondarySelectedCultivar of
        Just _ ->
            "532px"

        _ ->
            "276px"


selectedCultivarView : Model -> Cultivar -> Html Msg
selectedCultivarView model c =
    div
        [ style
            [ ( "min-width", selectionBoxWidth model )
            ]
        , class "selected-cultivar-box"
        ]
        [ div
            []
            [ div
                [ style
                    [ ( "display", "flex" )
                    , ( "flex-direction", "row" )
                    , ( "flex-wrap", "nowrap" )
                    ]
                ]
                [ maybeSecondarySelection model
                , selectedCultivarCard model c Primary
                ]
            ]
        ]


primaryCardMenu : Model -> Card.Block Msg
primaryCardMenu model =
    Card.menu
        [ css "width" "100%"
        , css "left" "0"
        , css "top" "14px"
        ]
        [ Button.render Mdl
            [ 0, 0 ]
            model.mdl
            [ Button.icon
            , Button.ripple
            , Options.onClick DismissSelectedCultivar
            , Color.background Color.primaryDark
            , Color.text Color.white
            , css "position" "absolute"
            , css "right" "16px"
            ]
            [ Icon.i "close" ]
        , Button.render Mdl
            [ 0, 0 ]
            model.mdl
            [ Button.icon
            , Button.ripple
            , Options.onClick PinSelectedCultivar
            , Color.background Color.primaryDark
            , Color.text Color.white
            , css "position" "absolute"
            , css "left" "16px"
            ]
            [ Icon.i "compare" ]
        ]

secondaryCardMenu : Model -> Card.Block Msg
secondaryCardMenu model =
    Card.menu [] []

selectedCultivarCard : Model -> Cultivar -> CultivarCardRole -> Html Msg
selectedCultivarCard model c role =
    Card.view
        [ Elevation.e6
        , cs "selected-cultivar-card"
        ]
        [ Card.title
            [ css "padding" "0"
            ]
            [ img
                [ style
                    [ ( "width", "256px" )
                    , ( "height", "158px" )
                    ]
                , src <| imgUrl c
                ]
                []
            , Card.head
                [ css "padding-left" "16px"
                , css "padding-top" "16px"
                , css "flex-direction" "row"
                , css "justify-content" "space-between"
                ]
                [ text c.name ]
            , Card.subhead
                [ css "padding-left" "16px"
                , css "font-style" "italic"
                ]
                [ text <| translatePlantType model c.plantType ]
            ]
        , case role of
            Primary ->
                primaryCardMenu model

            Secondary ->
                secondaryCardMenu model
        , Card.text
            [ css "padding-top" "0px" ]
            [ hr [] []
            , text <| Maybe.withDefault (tr model Phrases.DescriptionMissing) c.description
            ]
        ]


emptyNode : Html Msg
emptyNode =
    Html.text ""


cultivarListItemView : Model -> Cultivar -> Html Msg
cultivarListItemView model c =
    Card.view
        [ Options.onClick (SelectCultivar c.id)
        , css "width" "162px"
        , Color.background (Color.color Color.Green Color.S200)
        , css "margin" "8px"
        , Elevation.transition 250
        , if model.selectedCultivar == Just c.id then
            Elevation.e6
          else
            Elevation.e2
        ]
        [ Card.media
            [ css "background" ("url('" ++ (imgUrl c) ++ "') center / cover")
            , css "height" "100px"
            , css "width" "162px"
            ]
            []
        , Card.title
            [ css "padding" "8px"
            ]
            [ Card.head
                [ css "font-size" "16px"
                ]
                [ text c.name ]
            ]
        ]


cultivarListView : Model -> Html Msg
cultivarListView model =
    div
        [ style
            [ ( "display", "flex" )
            , ( "flex-direction", "column" )
            , ( "flex-grow", "0" )
            , ( "overflow-y", "auto" )
            ]
        ]
        [ div
            [ style
                [ ( "display", "flex" )
                , ( "flex-direction", "row" )
                , ( "flex-wrap", "wrap" )
                ]
            ]
            (List.map (cultivarListItemView model) model.cultivars)
        ]


view : Model -> Html Msg
view model =
    div
        -- Top layout is row, and fills up then height of view
        [ style
            [ ( "display", "flex" )
            , ( "flex-direction", "row" )
            , ( "height", "100%" )
            ]
        ]
        [ cultivarListView model
        , maybeSelectedCultivar model
        ]
