using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Carbon.Identity.Data.Migrations.IdentityServer.ConfigurationDb
{
    /// <inheritdoc />
    public partial class dataclientsRedirectUriupdate2 : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 6, 35, 4, 700, DateTimeKind.Utc).AddTicks(170));

            migrationBuilder.UpdateData(
                table: "ClientRedirectUris",
                keyColumn: "Id",
                keyValue: 2,
                column: "RedirectUri",
                value: "http://localhost:6002/docs/oauth2-redirect");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 6, 32, 8, 138, DateTimeKind.Utc).AddTicks(480));

            migrationBuilder.UpdateData(
                table: "ClientRedirectUris",
                keyColumn: "Id",
                keyValue: 2,
                column: "RedirectUri",
                value: "http://localhost:6002/docs/oauth2-redirect/");
        }
    }
}
